# Generated by Django 4.2.11 on 2024-04-21 14:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
        ("notifications", "0014_rename_new_level_notification_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="action_object_content_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_action_object_related",
                to="contenttypes.contenttype",
                verbose_name="action object content type",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="actor_content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_actor_related",
                to="contenttypes.contenttype",
                verbose_name="actor content type",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="recipient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to=settings.AUTH_USER_MODEL,
                verbose_name="recipient",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="target_content_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_target_related",
                to="contenttypes.contenttype",
                verbose_name="target content type",
            ),
        ),
    ]