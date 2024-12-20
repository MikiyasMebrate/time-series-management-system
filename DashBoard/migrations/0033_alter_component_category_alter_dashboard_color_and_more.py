# Generated by Django 4.2.6 on 2024-10-22 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0004_alter_quarterdata_indicator'),
        ('DashBoard', '0032_component_is_single_year_alter_component_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('card', 'card'), ('table', 'table'), ('graph', 'graph')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(blank=True, choices=[('green', 'green'), ('red', 'red'), ('blue', 'blue')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dashboardindicator',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='year', to='Base.datapoint'),
        ),
    ]
