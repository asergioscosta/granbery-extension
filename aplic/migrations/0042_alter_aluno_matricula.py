# Generated by Django 4.2.6 on 2023-10-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0041_pessoa_curso_alter_aluno_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=24168, unique=True, verbose_name='Matrícula'),
        ),
    ]
