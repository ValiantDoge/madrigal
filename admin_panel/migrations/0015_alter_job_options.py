# Generated by Django 4.1.2 on 2023-03-31 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0014_jobapplication_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['created_at']},
        ),
    ]
