# Generated by Django 4.2 on 2024-04-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_confirm"),
    ]

    operations = [
        migrations.AlterField(
            model_name="confirm",
            name="dropoffDate",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="confirm",
            name="pickupDate",
            field=models.DateTimeField(),
        ),
    ]
