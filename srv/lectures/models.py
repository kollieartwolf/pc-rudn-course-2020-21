from django.db import models
from django.utils import timezone
from django.urls import reverse


class OpenedLectures(models.Manager):
    def get_queryset(self):
        return super(OpenedLectures, self).get_queryset().filter(status='opened')


class Lecture(models.Model):
    # статусы лекций:
    STATUS_CHOICES = (('writing', 'В процессе'),
                      ('to_review', 'Требует проверки'),
                      ('opened', 'Открыта'),
                      )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    desc = models.TextField(max_length=250)
    status = models.CharField(max_length=9,
                              choices=STATUS_CHOICES,
                              default='writing')
    publish = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    opened = OpenedLectures()
    
    def get_absolute_url(self):
        return reverse('lectures:show_lecture', args=[self.slug])
    
    class Meta:
        ordering = ('publish',)
        db_table = 'lectures'

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = (('writing', 'В процессе'),
                      ('to_review', 'Требует проверки'),
                      ('ready', 'Готова'),
                      )
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=9,
                              choices=STATUS_CHOICES,
                              default='writing')
    publish = models.DateTimeField(default=timezone.now)
    lecture = models.ForeignKey(Lecture,
                                on_delete=models.CASCADE,
                                related_name='articles')
    
    class Meta:
        ordering = ('publish',)
        db_table = 'articles'
        
    def __str__(self):
        return self.title


class Section(models.Model):
    h2_title = models.CharField(max_length=100)
    h2_slug = models.SlugField(max_length=120)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='sections')
    
    class Meta:
        ordering = ('publish',)
        db_table = 'sections'
    
    def __str__(self):
        return self.h2_title
