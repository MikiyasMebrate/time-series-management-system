# Generated by Django 4.2.6 on 2024-11-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0048_rename_has_icons_component_has_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('graph', 'graph'), ('table', 'table'), ('card', 'card')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(blank=True, choices=[('blue', 'blue'), ('green', 'green'), ('red', 'red')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='style',
            field=models.CharField(choices=[('justify-content-end', 'End'), ('justify-content-start', 'Start'), ('justify-content-center', 'Center'), ('justify-content-between', 'Gap between')], default='justify-content-start', max_length=100),
        ),
    ]