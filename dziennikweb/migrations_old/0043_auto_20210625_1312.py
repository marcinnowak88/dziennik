# Generated by Django 3.2 on 2021-06-25 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0042_alter_grade_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.PositiveSmallIntegerField(choices=[(2, '3.5'), (3, '4.0'), (5, '5.0'), (0, '2.0'), (4, '4.5'), (1, '3.0')], default=0),
        ),
        migrations.AlterField(
            model_name='student2_course_grade',
            name='grade',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dziennikweb.grade'),
        ),
    ]