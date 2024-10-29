# Generated by Django 3.2.23 on 2024-10-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('price_per_gallon', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
