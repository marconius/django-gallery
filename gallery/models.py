from django.db import models
from django.db.models import permalink
from tagging.fields import TagField
from django.conf import settings
from django.utils.translation import ugettext as _

class Attribute(models.Model) :
    name = models.CharField(_('name'), max_length=100)
    
    class Meta :
       verbose_name = _('attribute')
       
    def __unicode__(self):
        return self.name

class Painting(models.Model) :
    STATUS_CHOICES = (
        (1, _('Live')),
        (2, _('Not Live')),
    )
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField()
    # Translators : this is the name of the field not the choice of flaging the item as live
    live = models.IntegerField(_('live'), choices = STATUS_CHOICES, default = 1)
    sort_order = models.IntegerField(_('sort order'), default = 0)
    image = models.FileField(_('main image'), upload_to = 'img/paintings/')
    preview = models.ImageField(_('preview image'), upload_to ='img/paintings/previews/', blank = 'true')
    description = models.TextField(_('description'), blank = True)
    attributes = models.ManyToManyField(Attribute, through = 'ItemAttribute', blank = True)
    tags = TagField(_('tags'))
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    sold = models.BooleanField(_('sold'))
    
    class Meta :
       verbose_name = _('painting')
       verbose_name_plural = _('paintings')
        
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
        (1, _('Live')),
        (2, _('Not Live')),
    )
    title = models.CharField(_('title'), max_length = 255)
    slug = models.SlugField()
    live = models.IntegerField(_('live'), choices = STATUS_CHOICES, default = 1)
    cover_painting = models.ForeignKey(Painting, blank = True, null = True)
    paintings = models.ManyToManyField(Painting, related_name='collections')
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    description = models.TextField(_('description'), blank = True)
    sort_order = models.IntegerField(_('sort order'), default=0)
    
    class Meta :
       verbose_name = _('collection')
    
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
      return ('collection_detail', None, { 'slug': self.slug })

class ItemAttribute(models.Model) :
    painting = models.ForeignKey(Painting)
    attribute = models.ForeignKey(Attribute)
    description = models.TextField()
    
