# Generated by Django 4.2.3 on 2023-10-10 01:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="profile_image",
            field=models.ImageField(null=True, upload_to="get_unique_filename"),
        ),
    ]