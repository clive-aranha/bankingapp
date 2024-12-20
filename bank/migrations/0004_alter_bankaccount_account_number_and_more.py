# Generated by Django 5.1.3 on 2024-11-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_bankaccount_alter_transaction_receiver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
