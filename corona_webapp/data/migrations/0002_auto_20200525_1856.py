# Generated by Django 3.0.1 on 2020-05-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beds', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitals', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ventilator',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('ventilators', models.IntegerField(default=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
