# Generated by Django 3.2 on 2021-06-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0043_auto_20210625_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.CharField(choices=[('5.0', '5.0'), ('4.5', '4.5'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0'), ('2.0', '2.0')], default=2.0, max_length=3),
        ),
    ]