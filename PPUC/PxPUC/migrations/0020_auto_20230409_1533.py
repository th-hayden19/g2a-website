# Generated by Django 3.1.3 on 2023-04-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PxPUC", "0019_auto_20230409_1526"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="keyword",
            name="provisions",
        ),
        migrations.AddField(
            model_name="provision",
            name="keywords",
            field=models.ManyToManyField(to="PxPUC.Keyword"),
        ),
    ]
