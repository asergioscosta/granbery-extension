# Generated by Django 4.2.5 on 2023-10-17 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0046_remove_equipe_aluno_remove_equipe_projeto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=66776, unique=True, verbose_name='Matrícula'),
        ),
    ]
