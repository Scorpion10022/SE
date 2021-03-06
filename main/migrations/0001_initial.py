# Generated by Django 3.1.7 on 2021-03-29 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=10)),
                ('exercise', models.CharField(max_length=10)),
                ('endurance_or_strength', models.CharField(max_length=10)),
                ('body_part', models.CharField(max_length=10)),
                ('problems', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('exercise', models.CharField(max_length=10)),
                ('endurance_or_strength', models.CharField(max_length=10)),
                ('body_part', models.CharField(max_length=10)),
                ('problems', models.CharField(max_length=10)),
            ],
        ),
    ]
