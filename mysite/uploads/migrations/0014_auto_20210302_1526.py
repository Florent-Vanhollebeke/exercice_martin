# Generated by Django 3.1.7 on 2021-03-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uploads", "0013_auto_20210302_1220"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="content",
            field=models.FileField(upload_to="documents/"),
        ),
        migrations.AlterField(
            model_name="person",
            name="first_name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="person",
            name="last_name",
            field=models.CharField(max_length=200),
        ),
    ]