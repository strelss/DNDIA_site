from django.db import models

class Progress_Work1(models.Model):
    header = models.CharField(blank=True, max_length=150, verbose_name='Название достижения')
    text = models.TextField(blank=True, max_length=2500, verbose_name='Текст достижения')
    img1 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №1')
    img2 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №2')
    img3 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №3')
    img4 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №4')
    img5 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №5')


    def __str__(self):
        return ('Объект достижений института №1')

    class Meta:
        verbose_name = 'Достижения института №1'
        verbose_name_plural = 'Достижения института №1'


class Progress_Work2(models.Model):
    header = models.CharField(blank=True, max_length=150, verbose_name='Название достижения')
    text = models.TextField(blank=True, max_length=2500, verbose_name='Текст достижения')
    img1 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №1')
    img2 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №2')
    img3 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №3')
    img4 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №4')
    img5 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №5')

    def __str__(self):
        return ('Объект достижений института №2')

    class Meta:
        verbose_name = 'Достижения института №2'
        verbose_name_plural = 'Достижения института №2'

class Progress_Work3(models.Model):
    header = models.CharField(blank=True, max_length=150, verbose_name='Название достижения')
    text = models.TextField(blank=True, max_length=2500, verbose_name='Текст достижения')
    img1 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №1')
    img2 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №2')
    img3 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №3')
    img4 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №4')
    img5 = models.ImageField(upload_to='media/progress', blank=True, verbose_name='Картинка достижения №5')

    def __str__(self):
        return ('Объект достижений института №3')

    class Meta:
        verbose_name = 'Достижения института №3'
        verbose_name_plural = 'Достижения института №3'


class Progress_Potencial(models.Model):
    doc = models.CharField(blank=True, max_length=5, verbose_name='Количеств докторов')
    kan = models.CharField(blank=True, max_length=5, verbose_name='Количеств кандидатов')

    def __str__(self):
        return ('Объект научного потенциала')

    class Meta:
        verbose_name = 'Научный потенциал'
        verbose_name_plural = 'Научный потенциал'

class Progress_Matbase(models.Model):
    header1 = models.CharField(blank=True, max_length=150, verbose_name='Название материальной базы №1')
    text1 = models.TextField(blank=True, max_length=2500, verbose_name='Описание материальной базы №1')
    img1_1 = models.ImageField(blank=True, upload_to='media/progress', verbose_name='Первая картинка материальной базы №1')
    img1_2 = models.ImageField(blank=True, upload_to='media/progress', verbose_name='Вторая картинка материальной базы №1')
    img1_3 = models.ImageField(blank=True, upload_to='media/progress',
                               verbose_name='Третья картинка материальной базы №1')



    header2 = models.CharField(blank=True, max_length=150, verbose_name='Название материальной базы №2')
    text2 = models.TextField(blank=True, max_length=2500, verbose_name='Описание материальной базы №2')
    img2_1 = models.ImageField(blank=True, upload_to='media/progress', verbose_name='Первая картинка материальной базы №2')
    img2_2 = models.ImageField(blank=True, upload_to='media/progress', verbose_name='Вторая картинка материальной базы №2')
    img2_3 = models.ImageField(blank=True, upload_to='media/progress',
                               verbose_name='Третья картинка материальной базы №2')


    header3 = models.CharField(blank=True, max_length=150, verbose_name='Название материальной базы №3')
    text3 = models.TextField(blank=True, max_length=2500, verbose_name='Описание материальной базы №3')
    img3_1 = models.ImageField(blank=True, upload_to='media/progress', verbose_name='Первая картинка материальной базы №3')
    img3_2 = models.ImageField(blank=True, upload_to='media/progress', verbose_name='Вторая картинка материальной базы №3')
    img3_3 = models.ImageField(blank=True, upload_to='media/progress',
                               verbose_name='Третья картинка материальной базы №3')


    header4 = models.CharField(blank=True, max_length=150, verbose_name='Название материальной базы №4')
    text4 = models.TextField(blank=True, max_length=2500, verbose_name='Описание материальной базы №4')
    img4_1 = models.ImageField(blank=True, upload_to='media/progress', verbose_name='Первая картинка материальной базы №4')
    img4_2 = models.ImageField(blank=True, upload_to='media/progress', verbose_name='Вторая картинка материальной базы №4')
    img4_3 = models.ImageField(blank=True, upload_to='media/progress',
                               verbose_name='Третья картинка материальной базы №4')

    def __str__(self):
        return ('Объект материальной базы')

    class Meta:
        verbose_name = 'Материальная база'
        verbose_name_plural = 'Материальная база'