# Generated by Django 4.2.6 on 2024-05-20 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Idiomas',
            },
        ),
        migrations.CreateModel(
            name='Frase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(default='Anónimo', max_length=50)),
                ('frase', models.TextField(blank=True, null=True)),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bases.idioma')),
            ],
            options={
                'verbose_name_plural': 'Frases',
            },
        ),
    ]