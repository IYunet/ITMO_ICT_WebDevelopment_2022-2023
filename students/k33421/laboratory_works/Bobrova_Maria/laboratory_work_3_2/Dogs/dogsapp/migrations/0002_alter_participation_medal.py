# Generated by Django 4.1.4 on 2022-12-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogsapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="participation",
            name="medal",
            field=models.CharField(
                choices=[("g", "gold"), ("s", "silver"), ("b", "bronze")],
                max_length=1,
                null=True,
            ),
        ),
    ]
