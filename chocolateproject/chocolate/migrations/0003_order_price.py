# Generated by Django 3.2.12 on 2022-06-01 23:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chocolate', '0002_auto_20220602_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
