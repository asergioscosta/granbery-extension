# Generated by Django 4.2.5 on 2023-10-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0064_remove_employee_department_employee_pessoa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=70993, unique=True, verbose_name='Matrícula'),
        ),
    ]