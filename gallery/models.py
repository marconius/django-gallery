from django.db import models
from django.db.models import permalink
from tagging.fields import TagField
from django.conf import settings

class Attribute(models.Model) :
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Painting(models.Model) :
    STATUS_CHOICES = (
        (1, 'Live'),
        (2, 'Not Live'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    live = models.IntegerField(choices = STATUS_CHOICES, default = 1)
    sort_order = models.IntegerField(default = 0)
    image = models.FileField(upload_to = 'img/paintings/')
    preview = models.ImageField(upload_to ='img/paintings/previews/', blank = 'true')
    description = models.TextField(blank = True)
    attributes = models.ManyToManyField(Attribute, through = 'ItemAttribute', blank = True)
    tags = TagField()
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    sold = models.BooleanField()
    
    #class Meta :
    #   ordering = ('-uploaded')
        
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ('painting_detail', (), { 'slug': self.slug })
    
    @property
    def url(self) :
        return '%s%s' % (settings.MEDIA_URL, self.image)
    
    @property
    def preview_url(self) :
        return '%s%s' % (settings.MEDIA_URL, self.preview)

class Collection(models.Model) :
    STATUS_CHOICES = (
        (1, 'Live'),
        (2, 'Not Live'),
    )
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    live = models.IntegerField(choices = STATUS_CHOICES, default = 1)
    cover_painting = models.ForeignKey('Painting', blank = True, null = True)
    paintings = models.ManyToManyField('Painting', related_name='collections')
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    description = models.TextField(blank = True)
    
    sort_order = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
      return ('collection_detail', None, { 'slug': self.slug })

class ItemAttribute(models.Model) :
    painting = models.ForeignKey(Painting)
    attribute = models.ForeignKey(Attribute)
    description = models.TextField()
    
