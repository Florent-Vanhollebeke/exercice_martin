# Generated by Django 3.1.7 on 2021-03-01 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("uploads", "0008_auto_20210301_1849"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="personmodel",
            name="user",
        ),
    ]
