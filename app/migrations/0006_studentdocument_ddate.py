# Generated by Django 4.1.2 on 2022-10-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_studentdocument_ddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdocument',
            name='Ddate',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ الوثيقة'),
        ),
    ]
