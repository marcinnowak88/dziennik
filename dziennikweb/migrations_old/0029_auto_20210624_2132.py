# Generated by Django 3.2 on 2021-06-24 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0028_auto_20210624_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.CharField(choices=[('5.0', '5.0'), ('4.5', '4.5'), ('3.5', '3.5'), ('3.0', '3.0'), ('2.0', '2.0'), ('4.0', '4.0')], default=2.0, max_length=3),
        ),
        migrations.AlterField(
            model_name='student2_course_grade',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]