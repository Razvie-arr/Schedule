# Generated by Django 3.1 on 2020-09-02 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ivtasu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveSmallIntegerField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')])),
                ('spisok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ivtasu.zanyatia', verbose_name='Список занятий в день')),
            ],
        ),
    ]
