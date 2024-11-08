# Generated by Django 4.2.6 on 2024-09-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0025_component_data_type_alter_component_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='configuration',
        ),
        migrations.AddField(
            model_name='component',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='components/'),
        ),
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.CharField(choices=[('graph', 'graph'), ('card', 'card')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(choices=[('red', 'red'), ('blue', 'blue'), ('green', 'green')], max_length=50),
        ),
    ]
