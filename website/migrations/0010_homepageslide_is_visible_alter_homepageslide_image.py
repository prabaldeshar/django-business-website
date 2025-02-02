# Generated by Django 5.1.5 on 2025-02-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_homepageslide'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepageslide',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='homepageslide',
            name='image',
            field=models.ImageField(upload_to='homepage_slides/'),
        ),
    ]
