# Generated by Django 4.2.6 on 2024-11-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0042_alter_component_category_alter_dashboard_color_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='row',
            options={'ordering': ['rank']},
        ),
        migrations.RenameField(
            model_name='component',
            old_name='has_json',
            new_name='is_country',
        ),
        migrations.RemoveField(
            model_name='component',
            name='json',
        ),
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('graph', 'graph'), ('card', 'card'), ('table', 'table')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(blank=True, choices=[('green', 'green'), ('red', 'red'), ('blue', 'blue')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='style',
            field=models.CharField(choices=[('justify-content-end', 'End'), ('justify-content-center', 'Center'), ('justify-content-between', 'Gap between'), ('justify-content-start', 'Start')], default='justify-content-start', max_length=100),
        ),
    ]
