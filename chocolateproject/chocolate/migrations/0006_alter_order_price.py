# Generated by Django 3.2.12 on 2022-06-02 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocolate', '0005_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.TextField(),
        ),
    ]
