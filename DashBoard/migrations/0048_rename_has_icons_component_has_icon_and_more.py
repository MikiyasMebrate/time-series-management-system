# Generated by Django 4.2.6 on 2024-11-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0047_component_has_icons_dashboardindicator_icon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='component',
            old_name='has_icons',
            new_name='has_icon',
        ),
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('card', 'card'), ('table', 'table'), ('graph', 'graph')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(blank=True, choices=[('green', 'green'), ('blue', 'blue'), ('red', 'red')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='style',
            field=models.CharField(choices=[('justify-content-end', 'End'), ('justify-content-center', 'Center'), ('justify-content-start', 'Start'), ('justify-content-between', 'Gap between')], default='justify-content-start', max_length=100),
        ),
    ]
