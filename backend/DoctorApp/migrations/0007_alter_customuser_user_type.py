# Generated by Django 5.0.3 on 2024-03-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DoctorApp", "0006_alter_customuser_user_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.IntegerField(
                choices=[(3, "User"), (2, "doc"), (1, "admin")], default=1
            ),
        ),
    ]