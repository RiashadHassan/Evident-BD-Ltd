# Generated by Django 4.2.4 on 2023-08-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_inputitems_inputitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputitem',
            name='input_numbers',
            field=models.CharField(max_length=200),
        ),
    ]
