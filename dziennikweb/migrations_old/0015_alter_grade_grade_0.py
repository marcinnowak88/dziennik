# Generated by Django 3.2 on 2021-06-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0014_auto_20210624_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade_0',
            field=models.PositiveSmallIntegerField(choices=[(2, '3.5'), (4, '4.5'), (3, '4.0'), (1, '3.0'), (0, '2.0'), (5, '5.0')], default=0),
        ),
    ]
