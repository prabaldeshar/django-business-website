# Generated by Django 5.1.5 on 2025-06-29 04:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0012_alter_aboutus_options_service_is_visible"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactInfo",
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
                (
                    "phone",
                    models.CharField(help_text="Contact phone number", max_length=20),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        help_text="Contact email address",
                        max_length=254,
                        null=True,
                    ),
                ),
                (
                    "facebook",
                    models.URLField(
                        blank=True, help_text="Facebook page URL", null=True
                    ),
                ),
                (
                    "instagram",
                    models.URLField(
                        blank=True, help_text="Instagram profile URL", null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Contact Information",
                "verbose_name_plural": "Contact Information",
            },
        ),
    ]
