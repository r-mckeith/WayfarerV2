# Generated by Django 3.1.7 on 2021-03-18 21:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_remove_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
