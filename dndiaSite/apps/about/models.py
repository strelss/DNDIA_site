from django.db import models

class About_History(models.Model):
    head_line = models.CharField(max_length=100, verbose_name='Заголовок исторической справки')
    history_text = models.TextField(max_length=5000, verbose_name='Текст исторической справки')
    img_history = models.ImageField(upload_to='media/history', verbose_name='Картинка для исторической справки')

    def __str__(self):
        return ('Объект исторической справки')

    class Meta:
        verbose_name = 'Историческая справка'
        verbose_name_plural = 'Исторические справки'

class About_Command(models.Model):
    img_com = models.ImageField(upload_to='media/team', verbose_name='Фотография командира')
    milit_rank_com = models.CharField(max_length=50, verbose_name='Воинское звание командира')
    mane_com = models.CharField(max_length=50, blank=True, verbose_name='Имя и фамилия командира')
    post_com = models.TextField(max_length=150, verbose_name='Название должности командира')

    img_polit = models.ImageField(upload_to='media/team', verbose_name='Фотография замполита')
    milit_rank_polit = models.CharField(max_length=50, verbose_name='Воинское званиез замполита')
    mane_polit = models.CharField(max_length=50, blank=True, verbose_name='Имя и фамилия замполита')
    post_polit = models.TextField(max_length=150, verbose_name='Название лолжности замполита')

    img_first = models.ImageField(upload_to='media/team', verbose_name='Фотография первого зама')
    milit_rank_first = models.CharField(max_length=50, verbose_name='Воинское звание первго зама')
    mane_first = models.CharField(max_length=50, blank=True, verbose_name='Имя и фамилия первого зама')
    post_first = models.TextField(max_length=150, verbose_name='Название лолжности первого зама')

    img_scintific = models.ImageField(upload_to='media/team', verbose_name='Фотография зама по науке')
    milit_rank_scintific = models.CharField(max_length=50, verbose_name='Воинское звание зама по науке')
    mane_scintific = models.CharField(max_length=50, blank=True, verbose_name='Имя и фамилия зама по науке')
    post_scintific = models.TextField(max_length=150, verbose_name='Название лолжности зама по науке')

    img_nov = models.ImageField(upload_to='media/team', verbose_name='Фотография начальника НОВ')
    milit_rank_nov = models.CharField(max_length=50, verbose_name='Воинское звание начальника НОВ')
    mane_nov = models.CharField(max_length=50, blank=True, verbose_name='Имя и фамилия начальника НОВ')
    post_nov = models.TextField(max_length=150, verbose_name='Название лолжности начальника НОВ')

    img_ndu1 = models.ImageField(upload_to='media/team', verbose_name='Фотография начальника НДУ-1')
    milit_rank_ndu1 = models.CharField(max_length=50, verbose_name='Воинское звание начальника НДУ-1')
    mane_ndu1 = models.CharField(max_length=50, blank=True, verbose_name='Имя и фамилия начальника НДУ-1')
    post_ndu1 = models.TextField(max_length=150, verbose_name='Название лолжности начальника НДУ-1')

    img_ndu2 = models.ImageField(upload_to='media/team', verbose_name='Фотография начальника НДУ-2')
    milit_rank_ndu2 = models.CharField(max_length=50, verbose_name='Воинское звание начальника НДУ-2')
    mane_ndu2 = models.CharField(max_length=50, blank=True, verbose_name='Имя и фамилия начальника НДУ-2')
    post_ndu2 = models.TextField(max_length=150, verbose_name='Название лолжности начальника НДУ-2')

    img_otd01 = models.ImageField(upload_to='media/team', verbose_name='Фотография начальника 01 отдела')
    milit_rank_otd01 = models.CharField(max_length=50, verbose_name='Воинское звание начальника 01 отдела')
    mane_otd01 = models.CharField(max_length=50, blank=True, verbose_name='Имя и фамилия начальника 01 отдела')
    post_otd01 = models.TextField(max_length=150, verbose_name='Название лолжности начальника 01 отдела')

    def __str__(self):
        return ('Объект командования')

    class Meta:
        verbose_name = 'Командование'

class About_Servise(models.Model):
    img_ias = models.ImageField(blank=True, upload_to='media/activity', verbose_name="Картинка на ИАС")
    name_ias = models.CharField(max_length=150, verbose_name='Заголовок ИАС')
    text_ias = models.TextField(max_length=2500, verbose_name='Описание ИАС')

    img_expluat = models.ImageField(blank=True, upload_to='media/activity', verbose_name="Картинка на ИАС")
    name_expluat = models.CharField(max_length=150, verbose_name='Заголовок ИАС')
    text_expluat = models.TextField(max_length=2500, verbose_name='Описание ИАС')

    img_pnp = models.ImageField(blank=True, upload_to='media/activity', verbose_name="Картинка на ИАС")
    name_pnp = models.CharField(max_length=150, verbose_name='Заголовок ИАС')
    text_pnp = models.TextField(max_length=2500, verbose_name='Описание ИАС')

    img_rem = models.ImageField(blank=True, upload_to='media/activity', verbose_name="Картинка на ИАС")
    name_rem = models.CharField(max_length=150, verbose_name='Заголовок ИАС')
    text_rem = models.TextField(max_length=2500, verbose_name='Описание ИАС')

    img_mod = models.ImageField(blank=True, upload_to='media/activity', verbose_name="Картинка на ИАС")
    name_mod = models.CharField(max_length=150, verbose_name='Заголовок ИАС')
    text_mod = models.TextField(max_length=2500, verbose_name='Описание ИАС')

    def __str__(self):
        return ('Объект направлений деятельности')


    class Meta:
        verbose_name = 'Направление деятельности'