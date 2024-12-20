# Generated by Django 5.1.3 on 2024-11-18 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0010_servicerequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='loan_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='loan_term',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
