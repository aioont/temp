# Generated by Django 4.0.5 on 2023-02-18 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0017_alter_becomevendor_options_alter_becomevendor_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='becomevendor',
            options={'verbose_name_plural': 'Become Vendors'},
        ),
        migrations.AlterField(
            model_name='becomevendor',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
