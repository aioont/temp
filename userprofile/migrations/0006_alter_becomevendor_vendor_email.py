# Generated by Django 4.0.5 on 2023-02-18 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_alter_becomevendor_vendor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='becomevendor',
            name='vendor_email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
