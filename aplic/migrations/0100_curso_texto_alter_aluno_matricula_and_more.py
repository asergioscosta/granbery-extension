# Generated by Django 4.2.6 on 2023-12-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0099_alter_aluno_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='texto',
            field=models.TextField(default=1, max_length=255, verbose_name='Texto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=77710, unique=True, verbose_name='Matrícula'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descricao',
            field=models.CharField(max_length=255, verbose_name='Descrição'),
        ),
    ]