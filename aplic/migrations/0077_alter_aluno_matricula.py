# Generated by Django 4.2.6 on 2023-11-13 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0076_alter_aluno_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=14795, unique=True, verbose_name='Matrícula'),
        ),
    ]
