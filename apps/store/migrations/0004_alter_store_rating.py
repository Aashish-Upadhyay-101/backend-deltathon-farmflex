# Generated by Django 4.1.4 on 2023-01-20 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_storeproduct_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='rating',
            field=models.PositiveIntegerField(default=1),
        ),
    ]