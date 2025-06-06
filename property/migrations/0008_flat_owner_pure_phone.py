# Generated by Django 2.2.24 on 2025-05-27 00:03

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='RU', verbose_name='Нормализованный номер телефона'),
        ),
    ]
