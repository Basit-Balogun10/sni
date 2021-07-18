from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

	class Meta:
		model = Account
		fields = ('email', 'username', 'firstname', 'lastname', 'password1', 'password2',)


class AccountAuthenticationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):
	firstname = forms.CharField(label='First name', required='false')
	lastname = forms.CharField(label='Last name', required='false')
	
	class Meta:
		model = Account
		fields = ('email', 'username', 'firstname', 'lastname')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)
	
	
	def clean_firstname(self):
		firstname = self.cleaned_data['firstname']
		return firstname
	
	
	def clean_lastname(self):
		lastname = self.cleaned_data['lastname']
		return lastname
