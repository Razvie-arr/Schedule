# Generated by Django 3.1 on 2020-09-03 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivtasu', '0004_auto_20200903_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zanyatia',
            name='lector',
            field=models.CharField(max_length=50, verbose_name='ФИО преподавателя'),
        ),
    ]
