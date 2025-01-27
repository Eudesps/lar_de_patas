# Generated by Django 5.1.4 on 2025-01-28 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0005_remove_animal_tutor_delete_tutoratual'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='especie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='animais.especie'),
            preserve_default=False,
        ),
    ]
