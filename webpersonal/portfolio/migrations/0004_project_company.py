# Generated by Django 4.1.1 on 2022-09-11 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_jobs_1_project_jobs_2_project_jobs_3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='company',
            field=models.CharField(default='default', max_length=200, verbose_name='Empresa'),
            preserve_default=False,
        ),
    ]