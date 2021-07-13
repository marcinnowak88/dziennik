# Generated by Django 3.2 on 2021-06-24 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0013_alter_grade_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='grade_0',
            field=models.PositiveSmallIntegerField(choices=[(2, '3.5'), (3, '4.0'), (0, '2.0'), (1, '3.0'), (5, '5.0'), (4, '4.5')], default=0),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dziennikweb.student'),
        ),
    ]
