# Generated by Django 3.0.5 on 2020-04-15 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [('applications', '0001_squashed_0022_auto_20200414_1352')]

    operations = [
        migrations.RemoveField(model_name='applicationtemplate', name='host_pattern')
    ]