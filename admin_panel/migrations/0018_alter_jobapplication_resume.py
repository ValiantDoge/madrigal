# Generated by Django 4.1.2 on 2023-04-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0017_alter_job_options_alter_jobapplication_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(blank=True, max_length=540, null=True, upload_to='resume/'),
        ),
    ]
