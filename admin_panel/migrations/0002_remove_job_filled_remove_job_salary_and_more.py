# Generated by Django 4.1.2 on 2023-03-03 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='filled',
        ),
        migrations.RemoveField(
            model_name='job',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='job',
            name='website',
        ),
    ]
