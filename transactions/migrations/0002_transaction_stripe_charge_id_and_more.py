# Generated by Django 5.0.6 on 2024-06-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='stripe_charge_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='stripe_payment_intent_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
