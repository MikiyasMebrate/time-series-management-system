# Generated by Django 4.2.6 on 2024-10-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0031_alter_component_category_alter_dashboard_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='is_single_year',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('table', 'table'), ('graph', 'graph'), ('card', 'card')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(blank=True, choices=[('red', 'red'), ('blue', 'blue'), ('green', 'green')], max_length=50, null=True),
        ),
    ]