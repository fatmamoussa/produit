# Generated by Django 4.2.6 on 2024-03-21 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0003_remove_produit_updated_at_produit_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='created_at',
        ),
    ]
