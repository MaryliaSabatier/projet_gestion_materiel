# Generated by Django 5.0.6 on 2024-05-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_materiel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='nom',
            field=models.CharField(default='aucun', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='prenom',
            field=models.CharField(default='aucun', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='salle',
            name='nom',
            field=models.CharField(default='aucun', max_length=100, null=True),
        ),
    ]
