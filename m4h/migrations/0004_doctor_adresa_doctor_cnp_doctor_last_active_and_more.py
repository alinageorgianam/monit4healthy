# Generated by Django 5.1 on 2024-11-25 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m4h', '0003_alter_doctor_cod_parafa_alter_profile_cod_parafa'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='adresa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='cnp',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_active',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='telefon',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='adresa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='cnp',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='id_doctor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctors', to='m4h.patient'),
        ),
        migrations.AddField(
            model_name='patient',
            name='last_active',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='telefon',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='cod_parafa',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cnp',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cod_parafa',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
