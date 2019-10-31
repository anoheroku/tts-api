from django.db import models


class Sign(models.Model):
    normal_form = models.CharField(verbose_name='слово в нормальной форме', max_length=128)
    file = models.FileField(upload_to='normal_form_img')

    def __str__(self):
        return self.normal_form
