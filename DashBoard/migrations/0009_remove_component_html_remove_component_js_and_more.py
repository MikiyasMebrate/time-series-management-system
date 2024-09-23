# Generated by Django 4.2.6 on 2024-09-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0008_component_path_alter_dashboard_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='html',
        ),
        migrations.RemoveField(
            model_name='component',
            name='js',
        ),
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('card', 'card'), ('graph', 'graph')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(choices=[('blue', 'blue'), ('green', 'green'), ('red', 'red')], max_length=50),
        ),
    ]