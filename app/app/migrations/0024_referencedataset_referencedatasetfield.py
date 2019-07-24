# Generated by Django 2.2.3 on 2019-07-11 07:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0023_delete_sourceschema'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('table_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField()),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('licence', models.CharField(blank=True, max_length=256, null=True)),
                ('restrictions_on_usage', models.TextField(blank=True, null=True)),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_to', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created+', to=settings.AUTH_USER_MODEL)),
                ('enquiries_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DataGrouping')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reference Data Set',
            },
        ),
        migrations.CreateModel(
            name='ReferenceDatasetField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('data_type', models.IntegerField(choices=[(1, 'Character field'), (2, 'Integer field'), (3, 'Float field'), (4, 'Date field'), (5, 'Time field'), (6, 'Datetime field'), (7, 'Boolean field')])),
                ('is_identifier', models.BooleanField(default=False, help_text='This field is the unique identifier for the record')),
                ('name', models.CharField(help_text='The name of the field. May only contain letters numbers and underscores (no spaces)', max_length=60, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z][a-zA-Z0-9_\\.]*$')])),
                ('description', models.TextField(blank=True, null=True)),
                ('required', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created+', to=settings.AUTH_USER_MODEL)),
                ('reference_dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='app.ReferenceDataset')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reference Data Set Field',
                'unique_together': {('reference_dataset', 'name')},
            },
        ),
    ]