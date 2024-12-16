# Generated by Django 5.1.4 on 2024-12-16 04:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lead_management", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="status",
            field=models.CharField(
                choices=[
                    ("new", "New"),
                    ("in_progress", "In Progress"),
                    ("won", "Won"),
                    ("lost", "Lost"),
                ],
                default="new",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="lead",
            name="phone",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="lead",
            name="source",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="salespipeline",
            name="stage",
            field=models.CharField(
                choices=[
                    ("new", "New"),
                    ("in_progress", "In Progress"),
                    ("won", "Won"),
                    ("lost", "Lost"),
                ],
                default="Lead",
                max_length=50,
            ),
        ),
    ]