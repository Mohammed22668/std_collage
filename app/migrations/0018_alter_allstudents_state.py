# Generated by Django 4.1.2 on 2022-11-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_allstudents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allstudents',
            name='state',
            field=models.BooleanField(blank=True, default='مباشرة', max_length=100, null=True, verbose_name='مباشرة'),
        ),
    ]
