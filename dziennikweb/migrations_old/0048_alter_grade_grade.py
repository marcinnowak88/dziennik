# Generated by Django 3.2 on 2021-06-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0047_auto_20210626_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.CharField(choices=[(5, '5.0'), (3, '4.0'), (0, '2.0'), (2, '3.5'), (1, '3.0'), (4, '4.5')], default=2.0, max_length=3),
        ),
    ]
