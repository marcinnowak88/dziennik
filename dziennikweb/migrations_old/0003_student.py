# Generated by Django 3.2 on 2021-06-16 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dziennikweb', '0002_auto_20210617_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
    ]
