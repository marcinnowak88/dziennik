# Generated by Django 3.2 on 2021-06-24 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0016_auto_20210624_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='student_course',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='dziennikweb.student'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.PositiveSmallIntegerField(choices=[(1, '3.0'), (0, '2.0'), (5, '5.0'), (3, '4.0'), (4, '4.5'), (2, '3.5')], default=0),
        ),
    ]