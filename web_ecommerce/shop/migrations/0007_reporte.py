# Generated by Django 5.0.4 on 2024-09-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_commande_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=400)),
                ('message', models.CharField(max_length=800)),
                ('added_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-added_date'],
            },
        ),
    ]
