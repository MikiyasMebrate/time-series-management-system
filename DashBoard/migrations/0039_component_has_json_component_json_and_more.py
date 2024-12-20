# Generated by Django 4.2.6 on 2024-11-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0038_alter_component_category_alter_dashboard_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='has_json',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='component',
            name='json',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('table', 'table'), ('card', 'card'), ('graph', 'graph')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(blank=True, choices=[('blue', 'blue'), ('green', 'green'), ('red', 'red')], max_length=50, null=True),
        ),
    ]
