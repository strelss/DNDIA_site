from django.db import models

class Contact(models.Model):
    contact_first_name = models.CharField('Имя', max_length = 50)
    contact_organization = models.CharField('Организация', max_length = 50)
    contact_email = models.CharField('E-mail адрес', max_length = 50)
    contact_massage = models.TextField('Текст сообщения', max_length=3000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_first_name

    class Meta:
        verbose_name = 'Оставленная заявка'
        verbose_name_plural = 'Оставленные заявки'
