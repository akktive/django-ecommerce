# Generated by Django 4.0.4 on 2022-06-01 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_order_m_remove_order_s_remove_product_m_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
