# Generated by Django 4.0.6 on 2022-07-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddMedicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('rate', models.IntegerField(max_length=255)),
            ],
        ),
    ]
