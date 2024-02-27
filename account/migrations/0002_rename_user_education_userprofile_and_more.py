# Generated by Django 5.0.2 on 2024-02-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='user',
            new_name='userProfile',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='user',
            new_name='userProfile',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='base_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userskills',
            old_name='user',
            new_name='userProfile',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='headline',
            field=models.CharField(max_length=300),
        ),
    ]