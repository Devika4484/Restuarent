# Generated by Django 4.1.2 on 2023-01-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(blank=True, max_length=30, null=True)),
                ('Lname', models.CharField(blank=True, max_length=30, null=True)),
                ('Uname', models.CharField(blank=True, max_length=30, null=True)),
                ('Email', models.CharField(blank=True, max_length=30, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
