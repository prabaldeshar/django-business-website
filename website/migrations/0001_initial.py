# Generated by Django 5.1.5 on 2025-01-27 04:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "client_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "completed_date",
                    models.DateField(
                        blank=True, default=datetime.date.today, null=True
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
