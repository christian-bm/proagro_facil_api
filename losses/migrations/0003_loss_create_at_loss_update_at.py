# Generated by Django 4.1 on 2022-08-29 21:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("losses", "0002_alter_loss_event_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="loss",
            name="create_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, editable=False
            ),
        ),
        migrations.AddField(
            model_name="loss",
            name="update_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]