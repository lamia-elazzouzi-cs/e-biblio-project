# Generated by Django 3.2.3 on 2021-05-17 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chercheur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Ouvrage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('auteurs', models.CharField(max_length=100)),
                ('editeur', models.CharField(max_length=100)),
                ('date_publication', models.CharField(max_length=100)),
                ('examplaires_dispo', models.IntegerField()),
                ('specialite', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_chercheur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_biblio_data.chercheur')),
                ('id_ouvrage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_biblio_data.ouvrage')),
            ],
        ),
    ]
