# Generated by Django 4.1.7 on 2023-02-23 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_review_feed_review_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="caption",
            new_name="rcaption",
        ),
    ]
