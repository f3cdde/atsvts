# Generated by Django 3.2.3 on 2021-06-07 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0006_auto_20210607_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspapersection',
            name='circulate_days',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newspapersection',
            name='deadline_days',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newspapersection',
            name='deadline_hour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newspapersection',
            name='maximum_height_budget',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='newspapersection',
            name='minimum_height',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
