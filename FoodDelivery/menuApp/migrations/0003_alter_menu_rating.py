# Generated by Django 4.1.5 on 2023-01-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuApp', '0002_alter_menu_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
