# Generated by Django 3.1.3 on 2023-04-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PxPUC", "0012_auto_20230409_1226"),
    ]

    operations = [
        migrations.AlterField(
            model_name="municipality",
            name="sqMiArea",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
