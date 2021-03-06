# Generated by Django 3.2 on 2021-06-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0034_auto_20210624_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, default='', to='dziennikweb.Student2'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.CharField(choices=[('5.0', '5.0'), ('4.5', '4.5'), ('2.0', '2.0'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0')], default=2.0, max_length=3),
        ),
        migrations.DeleteModel(
            name='Student2_course',
        ),
    ]
