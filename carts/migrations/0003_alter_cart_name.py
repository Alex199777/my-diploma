# Generated by Django 5.1.1 on 2024-10-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
