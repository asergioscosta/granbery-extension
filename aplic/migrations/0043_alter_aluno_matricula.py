# Generated by Django 4.2.5 on 2023-10-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0042_alter_aluno_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=47203, unique=True, verbose_name='Matrícula'),
        ),
    ]
