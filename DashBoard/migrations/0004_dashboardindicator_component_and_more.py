# Generated by Django 4.2.6 on 2024-09-21 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0003_alter_component_name_alter_dashboard_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardindicator',
            name='component',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='component', to='DashBoard.component'),
        ),
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('graph', 'graph'), ('card', 'card')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(choices=[('blue', 'blue'), ('red', 'red'), ('green', 'green')], max_length=50),
        ),
    ]
