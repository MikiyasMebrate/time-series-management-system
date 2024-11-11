# Generated by Django 4.2.6 on 2024-11-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0050_dashboardindicator_custom_value_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardindicator',
            name='has_image',
        ),
        migrations.RemoveField(
            model_name='dashboardindicator',
            name='is_custom',
        ),
        migrations.AddField(
            model_name='component',
            name='has_image',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='component',
            name='is_custom',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('graph', 'graph'), ('table', 'table'), ('card', 'card')], max_length=50),
        ),
        migrations.AlterField(
            model_name='row',
            name='style',
            field=models.CharField(choices=[('justify-content-start', 'Start'), ('justify-content-center', 'Center'), ('justify-content-end', 'End'), ('justify-content-between', 'Gap between')], default='justify-content-start', max_length=100),
        ),
    ]