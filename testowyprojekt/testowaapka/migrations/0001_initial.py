# Generated by Django 5.0.4 on 2024-04-04 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klasa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Klasy',
            },
        ),
        migrations.CreateModel(
            name='Uczen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=20)),
                ('nazwisko', models.CharField(max_length=30)),
                ('klasa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testowaapka.klasa')),
            ],
            options={
                'verbose_name_plural': 'Uczniowie',
            },
        ),
    ]
