# Generated by Django 4.1.2 on 2023-04-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0020_alter_jobapplication_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='response',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
