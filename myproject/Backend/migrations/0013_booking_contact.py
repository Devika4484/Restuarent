# Generated by Django 4.1.2 on 2023-01-03 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0012_staffdb_confirm_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Phone', models.CharField(blank=True, max_length=30, null=True)),
                ('Email', models.CharField(blank=True, max_length=30, null=True)),
                ('NPersons', models.IntegerField(blank=True, max_length=30, null=True)),
                ('Date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Subject', models.CharField(blank=True, max_length=50, null=True)),
                ('Message', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
