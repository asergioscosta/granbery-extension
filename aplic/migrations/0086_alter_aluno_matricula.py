# Generated by Django 4.2.5 on 2023-11-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0085_alter_aluno_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=16464, unique=True, verbose_name='Matrícula'),
        ),
    ]
