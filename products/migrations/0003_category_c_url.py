# Generated by Django 4.0.4 on 2022-05-31 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_m_id_order_m_rename_p_id_order_p_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='c_url',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
