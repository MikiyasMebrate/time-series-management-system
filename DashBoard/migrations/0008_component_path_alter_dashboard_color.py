# Generated by Django 4.2.6 on 2024-09-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0007_component_is_multiple_alter_component_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='color',
            field=models.CharField(choices=[('green', 'green'), ('blue', 'blue'), ('red', 'red')], max_length=50),
        ),
    ]
