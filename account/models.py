from account.tokens import account_activation_token

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


def writer_img_upload_location(instance, filename):
    file_path = 'writer_img/{writer_detail}/{writer_id}-{filename}'.format(
        writer_detail=str(instance.username) + '-' + str(instance.id), writer_id=str(instance.id), filename=filename)
    return file_path

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, firstname, lastname, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
        )

        user.firstname = user.firstname.capitalize()
        user.lastname = user.lastname.capitalize()
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, username, firstname, lastname, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            firstname=firstname,
            lastname=lastname,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.firstname = user.firstname.capitalize()
        user.lastname = user.lastname.capitalize()

        if settings.DEBUG:
            domain = "127.0.0.1:8000"
        else:
            domain = "synergynetworkinternational.pythonanywhere.com"

        user.save(using=self._db)
                    
        subject = 'Activate Your Synergy Network International Account'
        message = render_to_string('registration/account_activation_email.html', {
            'user': user,
            'domain': domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email, ])
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    firstname = models.CharField(max_length=30, unique=False, null=False, blank=False)
    lastname = models.CharField(max_length=30, unique=False, null=False, blank=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_writer = models.BooleanField(default=False)
    about = models.TextField(max_length=600, null=True, blank=True)
    image = models.ImageField(upload_to=writer_img_upload_location, null=True, blank=True)

    def fullname(self):
        return self.firstname + ' ' + self.lastname

    def clean(self):
        if self.is_writer == True and (self.about == '' or self.about is None):
            raise ValidationError({'about': _('About field cannot be empty if user is a writer')})
        if self.is_writer == True and not self.image:
            raise ValidationError({'image': _('Please upload an image for this writer')})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)


    class Meta:
        ordering = ['user', 'email_confirmed']


    def __str__(self):
        return self.user.email + ', ' + str(self.email_confirmed)

class WriterProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="writer_profile")


    class Meta:
        ordering = ['user']


    def __str__(self):
        return self.user.email

@receiver(post_save, sender=Account)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=Account)
def update_writer_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_writer:
            WriterProfile.objects.create(user=instance)
            instance.writer_profile.save()
    else:
        if instance.is_writer:
            WriterProfile.objects.get_or_create(user=instance)
            instance.writer_profile.save()

