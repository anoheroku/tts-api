from django.db import models


class Sign(models.Model):
    normal_form = models.CharField(verbose_name='слово в нормальной форме', max_length=128)
    image = models.ImageField(upload_to='normal_form_img')
    other = models.CharField(verbose_name='еще какие-то данные', max_length=256)

    def __str__(self):
        return self.normal_form
