# Generated by Django 5.1 on 2024-11-25 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m4h', '0002_doctor_cod_parafa_profile_cod_parafa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='cod_parafa',
            field=models.CharField(blank=True, default='555555', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cod_parafa',
            field=models.CharField(blank=True, default='555555', max_length=6, null=True),
        ),
    ]
