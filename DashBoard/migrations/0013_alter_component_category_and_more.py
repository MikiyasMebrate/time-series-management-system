# Generated by Django 4.2.6 on 2024-09-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0012_component_configuration_alter_component_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('graph', 'graph'), ('card', 'card')], max_length=50),
        ),
        migrations.AlterField(
            model_name='component',
            name='configuration',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(choices=[('green', 'green'), ('blue', 'blue'), ('red', 'red')], max_length=50),
        ),
    ]