# Generated by Django 3.0.7 on 2020-07-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]