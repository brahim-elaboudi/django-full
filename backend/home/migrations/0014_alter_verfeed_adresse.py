# Generated by Django 4.2 on 2023-05-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_module_modules_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verfeed',
            name='adresse',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
