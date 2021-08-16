# Generated by Django 3.1.5 on 2021-07-25 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210725_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='writer_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
