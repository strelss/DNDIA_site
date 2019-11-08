# Generated by Django 2.2.6 on 2019-11-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191031_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index_citation',
            name='home_citat1',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цитата для фонового рисунка №1'),
        ),
        migrations.AlterField(
            model_name='index_citation',
            name='home_citat2',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цитата для фонового рисунка №2'),
        ),
        migrations.AlterField(
            model_name='index_citation',
            name='home_citat3',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цитата для фонового рисунка №3'),
        ),
        migrations.AlterField(
            model_name='index_citation',
            name='home_citat4',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цитата для фонового рисунка №4'),
        ),
        migrations.AlterField(
            model_name='index_citation',
            name='home_citat5',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цитата для фонового рисунка №5'),
        ),
        migrations.AlterField(
            model_name='index_page',
            name='home_page1',
            field=models.ImageField(upload_to='media/home_pages', verbose_name='Фоновый рисунок №1'),
        ),
        migrations.AlterField(
            model_name='index_page',
            name='home_page2',
            field=models.ImageField(upload_to='media/home_pages', verbose_name='Фоновый рисунок №2'),
        ),
        migrations.AlterField(
            model_name='index_page',
            name='home_page3',
            field=models.ImageField(upload_to='media/home_pages', verbose_name='Фоновый рисунок №3'),
        ),
        migrations.AlterField(
            model_name='index_page',
            name='home_page4',
            field=models.ImageField(upload_to='media/home_pages', verbose_name='Фоновый рисунок №4'),
        ),
        migrations.AlterField(
            model_name='index_page',
            name='home_page5',
            field=models.ImageField(upload_to='media/home_pages', verbose_name='Фоновый рисунок №5'),
        ),
    ]
