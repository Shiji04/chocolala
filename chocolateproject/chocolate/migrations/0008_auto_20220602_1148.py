# Generated by Django 3.2.12 on 2022-06-02 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chocolate', '0007_alter_order_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chocolate',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
    ]
