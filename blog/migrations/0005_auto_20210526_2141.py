# Generated by Django 3.1.5 on 2021-05-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210526_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='new',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='reply',
            name='active',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='reply',
            name='new',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='false',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='good',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='new',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]