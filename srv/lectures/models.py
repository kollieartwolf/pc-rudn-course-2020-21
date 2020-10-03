from django.db import models
from django.utils import timezone
from django.urls import reverse


class OpenedManager(models.Manager):
    def get_queryset(self):
        return super(OpenedManager,
                     self).get_queryset().filter(status='opened')


class Post(models.Model):
    STATUS_CHOICES = (('unshown', 'Unshown'),
                      ('opened', 'Opened'),
                      )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    short_desc = models.TextField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='unshown')
    objects = models.Manager()
    opened = OpenedManager()

    def get_absolute_url(self):
        return reverse('lectures:post_detail',
                       args=[self.slug])

    class Meta:
        ordering = ('publish',)

        def __str__(self):
            return self.title
