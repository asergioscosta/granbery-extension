# Generated by Django 4.2.6 on 2023-10-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0009_remove_instituicao_endereco_endereco_instituicao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(choices=[('Administração', 'Administração'), ('Sistemas de Informação', 'Sistemas de Informação'), ('Psicologia', 'Psicologia'), ('Direito', 'Direito'), ('Educação Física', 'Educação Física')], max_length=30, verbose_name='Nome do Curso')),
                ('descricao', models.TextField(max_length=250, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('NB', 'Não Binário')], max_length=2),
        ),
    ]