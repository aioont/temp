# Generated by Django 4.0.5 on 2023-02-15 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_adminmessage_providermessage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceprovider',
            old_name='s_name',
            new_name='sp_name',
        ),
    ]