# Generated by Django 3.1.3 on 2023-04-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PxPUC", "0017_department_mcontractobj"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provision",
            name="keywords",
            field=models.ManyToManyField(related_name="keyw", to="PxPUC.Keyword"),
        ),
    ]