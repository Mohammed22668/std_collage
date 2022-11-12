# Generated by Django 4.1.2 on 2022-11-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_allstudents_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdocument',
            name='study',
            field=models.CharField(blank=True, choices=[('الصباحية', 'الصباحية'), ('المسائية', 'المسائية')], max_length=20, null=True, verbose_name='الدراسة'),
        ),
        migrations.AlterField(
            model_name='allstudents',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ المباشرة'),
        ),
        migrations.AlterField(
            model_name='allstudents',
            name='state',
            field=models.BooleanField(blank=True, default=True, max_length=100, null=True, verbose_name='مباشرة'),
        ),
    ]
