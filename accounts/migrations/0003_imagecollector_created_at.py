# Generated by Django 2.2.5 on 2020-04-19 15:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_imagecollector'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecollector',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]