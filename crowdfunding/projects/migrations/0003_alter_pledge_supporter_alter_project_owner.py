# Generated by Django 4.1.5 on 2023-01-17 10:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0002_pledge"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pledge",
            name="supporter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="supporter_pledges",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner_projects",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
