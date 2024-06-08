# Generated by Django 5.0.6 on 2024-06-06 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
        ),
    ]
