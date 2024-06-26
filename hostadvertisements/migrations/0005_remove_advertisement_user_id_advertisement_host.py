# Generated by Django 5.0.6 on 2024-06-15 14:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostadvertisements', '0004_rename_host_advertisement_user_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='user_id',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='host',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='advertise', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
