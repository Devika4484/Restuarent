# Generated by Django 4.1.2 on 2023-01-02 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0010_cdb_pdb_delete_booking_delete_menudb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='admindb',
            new_name='staffdb',
        ),
    ]