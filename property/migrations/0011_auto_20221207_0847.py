# Generated by Django 2.2.24 on 2022-12-07 05:47

from django.db import migrations


def move_data_flat_2_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20221207_0828'),
    ]

    operations = [
        migrations.RunPython(move_data_flat_2_owner)
    ]