# Generated by Django 4.0.5 on 2023-02-19 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_vendor_link_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='link_user',
        ),
    ]
