# Generated by Django 4.1.2 on 2023-03-26 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_alter_job_company_description_alter_job_company_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='qualification',
        ),
    ]
