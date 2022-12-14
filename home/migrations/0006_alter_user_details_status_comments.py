# Generated by Django 4.1 on 2022-09-03 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_user_details_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_details",
            name="status",
            field=models.CharField(
                choices=[
                    ("ACTIVE", "ACTIVE"),
                    ("NOT_ACTIVE", "NOT_ACTIVE"),
                    ("BANNED", "BANNED"),
                    ("DELETED", "DELETED"),
                ],
                default="NOT_ACTIVE",
                max_length=255,
            ),
        ),
        migrations.CreateModel(
            name="comments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.user_details",
                    ),
                ),
            ],
        ),
    ]
