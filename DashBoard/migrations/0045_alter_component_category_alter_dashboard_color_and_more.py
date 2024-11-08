# Generated by Django 4.2.6 on 2024-11-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0044_regions_alter_dashboard_color_alter_row_style_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('table', 'table'), ('graph', 'graph'), ('card', 'card')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(blank=True, choices=[('blue', 'blue'), ('green', 'green'), ('red', 'red')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='style',
            field=models.CharField(choices=[('justify-content-between', 'Gap between'), ('justify-content-start', 'Start'), ('justify-content-end', 'End'), ('justify-content-center', 'Center')], default='justify-content-start', max_length=100),
        ),
    ]
