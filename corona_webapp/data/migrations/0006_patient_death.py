# Generated by Django 3.0.1 on 2020-05-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_remove_patient_positive'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='death',
            field=models.IntegerField(default=2),
        ),
    ]
