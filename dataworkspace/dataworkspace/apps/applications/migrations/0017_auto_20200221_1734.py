# Generated by Django 2.2.10 on 2020-02-21 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [('applications', '0016_auto_20191216_1202')]

    operations = [
        migrations.AlterModelOptions(
            name='applicationinstance',
            options={
                'permissions': [
                    ('start_all_applications', 'Can start all applications'),
                    ('develop_visualisations', 'Can develop visualisations'),
                    ('access_appstream', 'Can access appstream'),
                ]
            },
        )
    ]
