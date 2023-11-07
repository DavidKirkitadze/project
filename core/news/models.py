from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=255)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date publication')
    them = models.ForeignKey('category', on_delete=models.PROTECT, null=True)

    def __str__ (self):
        return self.title

class category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__ (self):
        return self.name


    def  get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'A new news'