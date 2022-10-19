# Generated by Django 4.1 on 2022-08-07 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_loginmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmedicine',
            name='expiry',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='addmedicine',
            name='menu',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='addmedicine',
            name='mrp',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='addmedicine',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='addmedicine',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='addmedicine',
            name='rate',
            field=models.IntegerField(null=True),
        ),
    ]