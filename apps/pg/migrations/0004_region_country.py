# Generated by Django 2.2 on 2021-04-05 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0003_district_population'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pg.Country'),
            preserve_default=False,
        ),
    ]
