# Generated by Django 4.2.5 on 2023-10-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0062_alter_aluno_matricula_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=23582, unique=True, verbose_name='Matrícula'),
        ),
    ]