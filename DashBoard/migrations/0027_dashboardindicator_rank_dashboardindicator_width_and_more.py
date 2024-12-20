# Generated by Django 4.2.6 on 2024-09-25 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0026_remove_component_configuration_component_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardindicator',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dashboardindicator',
            name='width',
            field=models.CharField(choices=[('25%', '25%'), ('33%', '33%'), ('50%', '50%'), ('100%', '100%')], default='50%', max_length=50),
        ),
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('graph', 'graph'), ('card', 'card'), ('table', 'table')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(blank=True, choices=[('blue', 'blue'), ('green', 'green'), ('red', 'red')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='icon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
