# Generated by Django 3.1.5 on 2021-05-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210526_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='lastname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
