# Generated by Django 4.2 on 2023-04-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=5, max_digits=12)),
                ('quantity', models.DecimalField(decimal_places=5, max_digits=15)),
                ('total_price', models.DecimalField(decimal_places=5, max_digits=15)),
                ('fee', models.DecimalField(decimal_places=5, max_digits=10)),
                ('fee_coefficient', models.DecimalField(decimal_places=4, max_digits=5)),
                ('fee_asset', models.CharField(max_length=10)),
                ('side', models.CharField(choices=[('Buy', 'buy'), ('Sell', 'sell')], max_length=5)),
                ('time_stamp', models.DateTimeField()),
            ],
        ),
    ]