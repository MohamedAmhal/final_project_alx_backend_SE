# Generated by Django 5.0.4 on 2024-09-11 23:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('added_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-added_date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=5000)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='shop.category')),
            ],
            options={
                'ordering': ['-added_date'],
            },
        ),
    ]
