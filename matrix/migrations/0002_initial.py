# Generated by Django 4.0 on 2022-01-11 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matrix', '0001_initial'),
        ('standard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrix',
            name='ref_standard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standard.standard'),
        ),
    ]
