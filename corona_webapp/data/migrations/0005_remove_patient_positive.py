# Generated by Django 3.0.1 on 2020-05-26 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='positive',
        ),
    ]