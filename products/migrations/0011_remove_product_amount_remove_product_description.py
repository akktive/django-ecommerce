# Generated by Django 4.0.4 on 2022-06-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_order_customer_order_user_delete_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
