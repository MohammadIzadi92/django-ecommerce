# Generated by Django 4.2 on 2023-04-11 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6, validators=[django.core.validators.RegexValidator(message="Sex must be one of these two options 'male or female'.", regex='(male)|(female)')], verbose_name='sex'),
        ),
    ]
