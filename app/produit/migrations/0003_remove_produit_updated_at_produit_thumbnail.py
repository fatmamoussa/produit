# Generated by Django 4.2.6 on 2024-03-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_rename_product_produit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='produit',
            name='thumbnail',
            field=models.ImageField(default='default.png', upload_to='produit/%Y/%m/', verbose_name='Logo'),
        ),
    ]
