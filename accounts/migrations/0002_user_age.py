# Generated by Django 4.1 on 2022-09-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="age",
            field=models.PositiveIntegerField(default=1, verbose_name="나이"),
            preserve_default=False,
        ),
    ]
