# Generated by Django 5.0.6 on 2024-07-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0005_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
