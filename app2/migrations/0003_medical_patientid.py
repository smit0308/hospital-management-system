# Generated by Django 5.0.6 on 2024-07-04 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_laboratory_labstaff'),
    ]

    operations = [
        migrations.AddField(
            model_name='medical',
            name='patientid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app2.patient'),
        ),
    ]
