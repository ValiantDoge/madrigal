# Generated by Django 4.1.2 on 2023-04-11 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_pic',
        ),
    ]
