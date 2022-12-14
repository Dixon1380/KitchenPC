# Generated by Django 4.1.3 on 2022-11-25 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceChecker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_location', models.CharField(max_length=50)),
                ('item_availability', models.BooleanField()),
                ('item_quantity', models.IntegerField()),
            ],
        ),
    ]
