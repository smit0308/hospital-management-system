# Generated by Django 5.0.6 on 2024-06-18 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='specialization',
            field=models.CharField(max_length=100),
        ),
    ]
