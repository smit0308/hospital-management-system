# Generated by Django 5.0.6 on 2024-07-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratory',
            name='labstaff',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
