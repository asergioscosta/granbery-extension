# Generated by Django 4.2.5 on 2023-10-17 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0044_remove_pessoa_curso_curso_aluno_curso_professor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=34853, unique=True, verbose_name='Matrícula'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='aluno',
            field=models.ManyToManyField(max_length=5, to='aplic.aluno'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='professor',
            field=models.ManyToManyField(max_length=5, to='aplic.professor'),
        ),
    ]
