# Generated by Django 5.0.6 on 2024-06-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostadvertisements', '0005_remove_advertisement_user_id_advertisement_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='pictures',
            field=models.JSONField(default=list),
        ),
    ]