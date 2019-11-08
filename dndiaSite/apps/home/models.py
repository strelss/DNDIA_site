from django.db import models

class Index_Page(models.Model):
    home_page1 = models.ImageField(upload_to='media/home_pages', verbose_name='Фоновый рисунок №1')
    home_page2 = models.ImageField(upload_to='media/home_pages', verbose_name='Фоновый рисунок №2')
    home_page3 = models.ImageField(upload_to='media/home_pages', verbose_name='Фоновый рисунок №3')
    home_page4 = models.ImageField(upload_to='media/home_pages', verbose_name='Фоновый рисунок №4')
    home_page5 = models.ImageField(upload_to='media/home_pages', verbose_name='Фоновый рисунок №5')

    def __str__(self):
        return ('Объект фоновых рисунков')

    class Meta:
        verbose_name = 'Фоновый рисунок'
        verbose_name_plural = 'Фоновые рисунки'

class Index_Citation(models.Model):
    home_citat1 = models.CharField(max_length=150, blank=True, verbose_name='Цитата для фонового рисунка №1')
    home_citat2 = models.CharField(max_length=150, blank=True, verbose_name='Цитата для фонового рисунка №2')
    home_citat3 = models.CharField(max_length=150, blank=True, verbose_name='Цитата для фонового рисунка №3')
    home_citat4 = models.CharField(max_length=150, blank=True, verbose_name='Цитата для фонового рисунка №4')
    home_citat5 = models.CharField(max_length=150, blank=True, verbose_name='Цитата для фонового рисунка №5')

    def __str__(self):
        return ('Объект цитат')

    class Meta:
        verbose_name = 'Цитата на фоновом рисунке'
        verbose_name_plural = 'Цитаты на фоновых рисунках'

class Home_Partners(models.Model):
    text_partners = models.TextField(max_length=2500, blank=True, verbose_name='Текст сотрудничества')
    img_partners = models.ImageField(blank=True, upload_to='media/home_pages', verbose_name='Картинка сотрудничества')

    def __str__(self):
        return ('Объект сотрудничества')

    class Meta:
        verbose_name = 'Сотрудничество'
        verbose_name_plural = 'Сотрудничество'

class Home_BukletPapers(models.Model):
    papers = models.FileField(blank=True, null=True, upload_to='media/bukPaper/papers_%Y%m%D', verbose_name='Сборник научных статей')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ('Объект статей')

    class Meta:
        verbose_name = 'Cборник научных статей'
        verbose_name_plural = 'Cборники научных статей'
        ordering = ['-date_pub']


class Home_Buklet(models.Model):
    buklet = models.FileField(blank=True, null=True, upload_to='media/bukPaper/buklet_%Y%m%D', verbose_name='Буклет института')

    def __str__(self):
        return ('Объект буклета')

    class Meta:
        verbose_name = 'Буклет'
        verbose_name_plural = 'Буклеты'
