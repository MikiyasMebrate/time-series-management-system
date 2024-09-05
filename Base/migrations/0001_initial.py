# Generated by Django 4.2 on 2024-09-04 14:44

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import fontawesome_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ENG', models.CharField(max_length=300, unique=True)),
                ('name_AMH', models.CharField(max_length=300, unique=True)),
                ('is_dashboard_visible', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_EC', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('year_GC', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('is_interval', models.BooleanField(default=False)),
                ('year_start_EC', models.CharField(blank=True, max_length=50, null=True)),
                ('year_start_GC', models.CharField(blank=True, max_length=50, null=True)),
                ('year_end_EC', models.CharField(blank=True, max_length=50, null=True)),
                ('year_end_GC', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['year_EC'],
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ENG', models.CharField(max_length=300)),
                ('title_AMH', models.CharField(blank=True, max_length=300, null=True)),
                ('composite_key', models.CharField(max_length=300, unique=True)),
                ('measurement_units', models.CharField(blank=True, max_length=50, null=True)),
                ('kpi_characteristics', models.CharField(blank=True, choices=[('inc', 'Increasing'), ('dec', 'Decreasing'), ('const', 'Constant')], max_length=10, null=True)),
                ('is_dashboard_visible', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('for_category', models.ManyToManyField(related_name='indicators', to='Base.category')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Base.indicator')),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_ENG', models.CharField(max_length=50)),
                ('month_AMH', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ENG', models.CharField(max_length=50)),
                ('title_AMH', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ENG', models.CharField(max_length=50)),
                ('title_AMH', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ENG', models.CharField(max_length=300, unique=True)),
                ('title_AMH', models.CharField(max_length=300, null=True)),
                ('icon', fontawesome_5.fields.IconField(blank=True, max_length=60)),
                ('is_dashboard', models.BooleanField(default=False)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QuarterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance', models.FloatField(blank=True, null=True)),
                ('target', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('for_datapoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.datapoint')),
                ('for_quarter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.quarter')),
                ('indicator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.indicator')),
            ],
        ),
        migrations.CreateModel(
            name='MonthData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance', models.FloatField(blank=True, null=True)),
                ('target', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('for_datapoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.datapoint')),
                ('for_month', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.month')),
                ('indicator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.indicator')),
            ],
        ),
        migrations.CreateModel(
            name='Indicator_Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_actual', models.BooleanField()),
                ('for_datapoint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.datapoint')),
                ('for_indicator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.indicator')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ENG', models.CharField(max_length=300, unique=True)),
                ('title_AMH', models.CharField(max_length=300, null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('file', models.FileField(upload_to='documents/')),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.topic')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.topic'),
        ),
        migrations.CreateModel(
            name='AnnualData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance', models.FloatField(blank=True, null=True)),
                ('target', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('for_datapoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.datapoint')),
                ('indicator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.indicator')),
            ],
        ),
    ]
