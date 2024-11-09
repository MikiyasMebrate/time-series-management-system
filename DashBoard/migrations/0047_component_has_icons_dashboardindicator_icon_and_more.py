# Generated by Django 4.2.6 on 2024-11-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0046_remove_dashboardindicator_regions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='has_icons',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dashboardindicator',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='dashboard/icon'),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(blank=True, choices=[('red', 'red'), ('blue', 'blue'), ('green', 'green')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='style',
            field=models.CharField(choices=[('justify-content-start', 'Start'), ('justify-content-center', 'Center'), ('justify-content-between', 'Gap between'), ('justify-content-end', 'End')], default='justify-content-start', max_length=100),
        ),
    ]
