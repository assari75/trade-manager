# Generated by Django 4.2 on 2023-04-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='side',
            field=models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=5),
        ),
    ]