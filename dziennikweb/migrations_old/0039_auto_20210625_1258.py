# Generated by Django 3.2 on 2021-06-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0038_auto_20210625_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='student2_course_grade',
            name='aaa',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.PositiveSmallIntegerField(choices=[(4, '4.5'), (5, '5.0'), (3, '4.0'), (1, '3.0'), (0, '2.0'), (2, '3.5')], default=0),
        ),
    ]