# Generated by Django 3.2 on 2021-06-17 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0009_auto_20210617_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_image',
            new_name='image_s',
        ),
    ]