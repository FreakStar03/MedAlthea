# Generated by Django 4.0.1 on 2022-01-29 13:56

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_remove_medical_id_medical_medicalid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]