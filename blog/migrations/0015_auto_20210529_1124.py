# Generated by Django 3.1.5 on 2021-05-29 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210527_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_body',
        ),
    ]
