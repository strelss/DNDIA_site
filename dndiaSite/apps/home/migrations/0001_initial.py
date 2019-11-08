# Generated by Django 2.2.6 on 2019-10-31 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index_Citation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_citat1', models.CharField(blank=True, max_length=50)),
                ('home_citat2', models.CharField(blank=True, max_length=50)),
                ('home_citat3', models.CharField(blank=True, max_length=50)),
                ('home_citat4', models.CharField(blank=True, max_length=50)),
                ('home_citat5', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Index_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_page1', models.ImageField(upload_to='media/home_pages')),
                ('home_page2', models.ImageField(upload_to='media/home_pages')),
                ('home_page3', models.ImageField(upload_to='media/home_pages')),
                ('home_page4', models.ImageField(upload_to='media/home_pages')),
                ('home_page5', models.ImageField(upload_to='media/home_pages')),
            ],
        ),
    ]
