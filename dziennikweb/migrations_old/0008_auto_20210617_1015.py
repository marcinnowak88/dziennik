# Generated by Django 3.2 on 2021-06-17 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0007_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses_image'),
        ),
        migrations.AddField(
            model_name='student',
            name='image_s',
            field=models.ImageField(blank=True, null=True, upload_to='students_image'),
        ),
    ]