# Generated by Django 5.0.6 on 2024-06-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostadvertisements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='pictures',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='map_location',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='thumbnail_picture',
            field=models.TextField(),
        ),
    ]