# Generated by Django 2.2.6 on 2019-11-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_com', models.ImageField(upload_to='media/team', verbose_name='Фотография командира')),
                ('milit_rank_com', models.CharField(max_length=50, verbose_name='Воинское звание командира')),
                ('post_com', models.TextField(max_length=150, verbose_name='Название должности командира')),
                ('img_polit', models.ImageField(upload_to='media/team', verbose_name='Фотография замполита')),
                ('milit_rank_polit', models.CharField(max_length=50, verbose_name='Воинское званиез замполита')),
                ('post_polit', models.TextField(max_length=150, verbose_name='Название лолжности замполита')),
                ('img_first', models.ImageField(upload_to='media/team', verbose_name='Фотография первого зама')),
                ('milit_rank_first', models.CharField(max_length=50, verbose_name='Воинское звание первго зама')),
                ('post_first', models.TextField(max_length=150, verbose_name='Название лолжности первого зама')),
                ('img_scintific', models.ImageField(upload_to='media/team', verbose_name='Фотография зама по науке')),
                ('milit_rank_scintific', models.CharField(max_length=50, verbose_name='Воинское звание зама по науке')),
                ('post_scintific', models.TextField(max_length=150, verbose_name='Название лолжности зама по науке')),
                ('img_nov', models.ImageField(upload_to='media/team', verbose_name='Фотография начальника НОВ')),
                ('milit_rank_nov', models.CharField(max_length=50, verbose_name='Воинское звание начальника НОВ')),
                ('post_nov', models.TextField(max_length=150, verbose_name='Название лолжности начальника НОВ')),
                ('img_ndu1', models.ImageField(upload_to='media/team', verbose_name='Фотография начальника НДУ-1')),
                ('milit_rank_ndu1', models.CharField(max_length=50, verbose_name='Воинское звание начальника НДУ-1')),
                ('post_ndu1', models.TextField(max_length=150, verbose_name='Название лолжности начальника НДУ-1')),
                ('img_ndu2', models.ImageField(upload_to='media/team', verbose_name='Фотография начальника НДУ-2')),
                ('milit_rank_ndu2', models.CharField(max_length=50, verbose_name='Воинское звание начальника НДУ-2')),
                ('post_ndu2', models.TextField(max_length=150, verbose_name='Название лолжности начальника НДУ-2')),
                ('img_otd01', models.ImageField(upload_to='media/team', verbose_name='Фотография начальника 01 отдела')),
                ('milit_rank_otd01', models.CharField(max_length=50, verbose_name='Воинское звание начальника 01 отдела')),
                ('post_otd01', models.TextField(max_length=150, verbose_name='Название лолжности начальника 01 отдела')),
            ],
            options={
                'verbose_name': 'Командование',
            },
        ),
    ]
