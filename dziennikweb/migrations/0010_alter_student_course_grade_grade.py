# Generated by Django 3.2 on 2021-06-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0009_alter_student_course_grade_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_course_grade',
            name='grade',
            field=models.CharField(choices=[('2.0', '2.0'), ('4.0', '4.0'), ('3.0', '3.0'), ('4.5', '4.5'), ('3.5', '3.5'), ('5.0', '5.0')], default=2.0, max_length=3),
        ),
    ]
