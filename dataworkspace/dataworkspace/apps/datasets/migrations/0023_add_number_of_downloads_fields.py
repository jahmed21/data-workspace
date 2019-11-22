# Generated by Django 2.2.4 on 2019-11-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('datasets', '0022_joint_datasets_linked_field_name_change')]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='number_of_downloads',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='referencedataset',
            name='number_of_downloads',
            field=models.PositiveIntegerField(default=0),
        ),
    ]