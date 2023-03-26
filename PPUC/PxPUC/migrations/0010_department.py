# Generated by Django 3.1.3 on 2023-03-26 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PxPUC", "0009_auto_20220812_2225"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deptName", models.CharField(max_length=50, null=True)),
                ("webLink", models.CharField(max_length=100, null=True)),
                ("fullOfficers2019", models.IntegerField()),
                ("partOfficers2019", models.IntegerField()),
                ("hasBill", models.BooleanField()),
            ],
        ),
    ]
