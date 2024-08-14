# Generated by Django 5.1b1 on 2024-08-09 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m4h', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='Necunoscut', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='id_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to='m4h.profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_active',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default='Necunoscut', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='adresa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nume',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prenume',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('doctor', 'Doctor'), ('pacient', 'Pacient')], max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telefon',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]