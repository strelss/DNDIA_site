# Generated by Django 2.2.6 on 2019-11-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20191103_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Servise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_ias', models.ImageField(upload_to='media/activity', verbose_name='Картинка на ИАС')),
                ('name_ias', models.CharField(max_length=150, verbose_name='Заголовок ИАС')),
                ('text_ias', models.TextField(max_length=2500, verbose_name='Описание ИАС')),
                ('img_expluat', models.ImageField(upload_to='media/activity', verbose_name='Картинка на ИАС')),
                ('name_expluat', models.CharField(max_length=150, verbose_name='Заголовок ИАС')),
                ('text_expluat', models.TextField(max_length=2500, verbose_name='Описание ИАС')),
                ('img_pnp', models.ImageField(upload_to='media/activity', verbose_name='Картинка на ИАС')),
                ('name_pnp', models.CharField(max_length=150, verbose_name='Заголовок ИАС')),
                ('text_pnp', models.TextField(max_length=2500, verbose_name='Описание ИАС')),
                ('img_rem', models.ImageField(upload_to='media/activity', verbose_name='Картинка на ИАС')),
                ('name_rem', models.CharField(max_length=150, verbose_name='Заголовок ИАС')),
                ('text_rem', models.TextField(max_length=2500, verbose_name='Описание ИАС')),
                ('img_mod', models.ImageField(upload_to='media/activity', verbose_name='Картинка на ИАС')),
                ('name_mod', models.CharField(max_length=150, verbose_name='Заголовок ИАС')),
                ('text_mod', models.TextField(max_length=2500, verbose_name='Описание ИАС')),
            ],
            options={
                'verbose_name': 'Направление деятельности',
            },
        ),
        migrations.AlterField(
            model_name='about_command',
            name='mane_ndu2',
            field=models.CharField(blank=True, max_length=50, verbose_name='Имя и фамилия начальника НДУ-2'),
        ),
    ]
