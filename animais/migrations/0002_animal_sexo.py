# Generated by Django 5.1.4 on 2025-01-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('M', 'Macho'), ('F', 'Fêmea')], default='M', max_length=1),
        ),
    ]