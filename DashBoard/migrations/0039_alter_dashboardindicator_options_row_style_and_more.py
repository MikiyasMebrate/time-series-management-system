# Generated by Django 4.2.6 on 2024-11-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0038_alter_component_category_alter_dashboard_color_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dashboardindicator',
            options={'ordering': ['rank']},
        ),
        migrations.AddField(
            model_name='row',
            name='style',
            field=models.CharField(choices=[('justify-content-end', 'End'), ('justify-content-center', 'Center'), ('justify-content-start', 'Start'), ('justify-content-between', 'Gap between')], default='justify-content-center', max_length=100),
        ),
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('graph', 'graph'), ('table', 'table'), ('card', 'card')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(blank=True, choices=[('red', 'red'), ('green', 'green'), ('blue', 'blue')], max_length=50, null=True),
        ),
    ]