# Generated by Django 5.1.1 on 2024-10-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_payment_order_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Нaзвание'),
        ),
    ]
