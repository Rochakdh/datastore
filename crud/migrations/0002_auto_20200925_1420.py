# Generated by Django 3.1.1 on 2020-09-25 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaldetails',
            old_name='adderss',
            new_name='address',
        ),
    ]