# Generated by Django 3.2.8 on 2021-10-16 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Personagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('apelidos', models.CharField(max_length=500)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1)),
                ('idade', models.IntegerField()),
                ('episodio_estreia', models.IntegerField()),
                ('altura', models.FloatField(help_text='Altura em Metros')),
                ('peso', models.IntegerField(help_text='Peso em kilos')),
                ('imagem', models.ImageField(help_text='Imagem do personagem', max_length=600, upload_to='')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo', to='kimetsu_app.grupo')),
                ('raca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raca', to='kimetsu_app.raca')),
            ],
        ),
    ]