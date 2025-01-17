# Generated by Django 2.2.24 on 2022-12-04 00:54

from django.db import migrations
import phonenumbers


def serialise_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        phone_number = flat.owners_phonenumber
        edited_number = phonenumbers.parse(phone_number, 'RU')
        if phonenumbers.is_valid_number(edited_number):
            flat.owner_pure_phone = phonenumbers.format_number(edited_number, phonenumbers.PhoneNumberFormat.E164)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20221204_0222'),
    ]

    operations = [
        migrations.RunPython(serialise_phonenumber),
    ]
