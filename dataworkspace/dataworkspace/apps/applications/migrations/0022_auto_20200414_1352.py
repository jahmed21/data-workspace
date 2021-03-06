# Generated by Django 3.0.5 on 2020-04-14 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('applications', '0021_applicationinstance_commit_id')]

    operations = [
        migrations.RemoveIndex(
            model_name='applicationtemplate', name='app_applica_host_ex_7bfb56_idx'
        ),
        migrations.RenameField(
            model_name='applicationtemplate',
            old_name='host_exact',
            new_name='host_basename',
        ),
        migrations.AlterField(
            model_name='applicationtemplate',
            name='host_basename',
            field=models.CharField(
                max_length=128, blank=False, null=False, unique=True
            ),
        ),
        migrations.AddIndex(
            model_name='applicationtemplate',
            index=models.Index(
                fields=['host_basename'], name='app_applica_host_ba_d9ab7e_idx'
            ),
        ),
    ]
