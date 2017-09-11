from django.db import models


class Course(models.Model):
    title = models.CharField('título', max_length=255)
    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'


class Review(models.Model):
    course = models.ForeignKey(Course, related_name='reviews', verbose_name='curso')
    name = models.CharField('nome', max_length=255)
    email = models.EmailField('e-mail')
    comment = models.TextField('comentário', blank=True, default='')
    rating = models.IntegerField('classificação')
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'course']

    def __str__(self):
        return '{0.rating} by {0.email} for {0.course}'.format(self)
