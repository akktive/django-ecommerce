# Generated by Django 4.0.4 on 2022-06-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_category_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(default='placeholder.png', max_length=50),
        ),
    ]
