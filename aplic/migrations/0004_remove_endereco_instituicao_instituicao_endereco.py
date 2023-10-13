# Generated by Django 4.2.6 on 2023-10-08 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_instituicao_endereco_instituicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='instituicao',
        ),
        migrations.AddField(
            model_name='instituicao',
            name='endereco',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='aplic.endereco'),
            preserve_default=False,
        ),
    ]