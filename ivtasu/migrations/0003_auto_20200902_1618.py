# Generated by Django 3.1 on 2020-09-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivtasu', '0002_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='day',
            field=models.SmallIntegerField(choices=[]),
        ),
    ]