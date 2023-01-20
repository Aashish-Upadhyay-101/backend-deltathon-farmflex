# Generated by Django 4.1.4 on 2023-01-20 02:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='image',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('duration', models.CharField(max_length=128)),
                ('quantity', models.PositiveBigIntegerField(default=0)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_store', to='store.store')),
                ('store_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_store_product', to='store.storeproduct')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
