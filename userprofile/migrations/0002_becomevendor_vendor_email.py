# Generated by Django 4.0.5 on 2023-02-18 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='becomevendor',
            name='vendor_email',
            field=models.EmailField(default='vendor@gmail.com', max_length=100),
        ),
    ]
