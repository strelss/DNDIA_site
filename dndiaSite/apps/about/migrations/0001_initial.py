# Generated by Django 2.2.6 on 2019-11-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_line', models.CharField(max_length=100, verbose_name='Заголовок исторической справки')),
                ('history_text', models.TextField(max_length=5000, verbose_name='Текст исторической справки')),
                ('img_history', models.ImageField(upload_to='media/history', verbose_name='Картинка для исторической справки')),
            ],
            options={
                'verbose_name': 'Историческая справка',
                'verbose_name_plural': 'Исторические справки',
            },
        ),
    ]
