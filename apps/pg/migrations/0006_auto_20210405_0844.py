# Generated by Django 2.2 on 2021-04-05 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0005_auto_20210405_0841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='regional_center',
            new_name='capital',
        ),
    ]
