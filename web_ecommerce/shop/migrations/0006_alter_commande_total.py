# Generated by Django 5.0.4 on 2024-09-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_commande_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='total',
            field=models.CharField(default=2265, max_length=200),
            preserve_default=False,
        ),
    ]
