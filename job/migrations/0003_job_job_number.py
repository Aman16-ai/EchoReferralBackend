# Generated by Django 5.0.2 on 2024-03-05 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_link_alter_job_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
