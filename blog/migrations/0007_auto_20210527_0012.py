# Generated by Django 3.1.5 on 2021-05-26 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210527_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='reviewed',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]