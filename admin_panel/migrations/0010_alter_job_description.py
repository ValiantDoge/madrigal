# Generated by Django 4.1.2 on 2023-03-28 11:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0009_jobapplication_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
