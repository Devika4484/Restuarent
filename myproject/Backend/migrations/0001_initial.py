# Generated by Django 4.1.2 on 2022-12-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admindb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Email', models.CharField(blank=True, max_length=30, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Username', models.CharField(blank=True, max_length=30, null=True)),
                ('Password', models.CharField(blank=True, max_length=30, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Profile')),
            ],
        ),
    ]
