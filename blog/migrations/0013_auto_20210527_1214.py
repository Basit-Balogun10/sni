# Generated by Django 3.1.5 on 2021-05-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210527_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='reply',
            name='body',
            field=models.TextField(default=None),
        ),
    ]
