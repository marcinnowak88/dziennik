# Generated by Django 3.2 on 2021-06-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0012_auto_20210620_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.PositiveSmallIntegerField(choices=[(3, '4.0'), (5, '5.0'), (4, '4.5'), (2, '3.5'), (1, '3.0'), (0, '2.0')], default=0),
        ),
    ]
