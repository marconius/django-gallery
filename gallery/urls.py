from django.conf.urls.defaults import *
from gallery.models import *

urlpatterns = patterns('gallery.views',
    
    url (r'^$',
        view='collection_list',
        name='gallery_home',
    ),
    
    url(r'^collections/(?P<slug>[-\w]+)/$',
        view='collection_detail',
        name='collection_detail',
    ),
        
    url(r'^(?P<slug>[-\w]+)/$',
        view='painting_detail',
        name='painting_detail',
    ),
    
)
