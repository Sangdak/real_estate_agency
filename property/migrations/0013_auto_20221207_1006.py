# Generated by Django 2.2.24 on 2022-12-07 07:06

from django.db import migrations


def add_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all().iterator():
        owner_dep = flat.owner_deprecated
        owner = Owner.objects.filter(owner=owner_dep).first()
        owner.flats.add(flat)
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20221207_0950'),
    ]

    operations = [
        migrations.RunPython(add_flats)
    ]
