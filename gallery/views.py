import datetime
import re

from django.shortcuts import get_object_or_404
from django.views.generic import list_detail

from gallery.models import *

def collection_list(request, **kwargs) :
    return list_detail.object_list (
        request,
        queryset=Collection.objects.all(),
        **kwargs
    )

def collection_detail(request, slug, template_name = "gallery/collection_detail.html", **kwargs):
    
    collection = get_object_or_404(Collection, slug__iexact = slug)
    
    return list_detail.object_list (
        request,
        queryset=collection.paintings.all(),
        template_name=template_name,
        extra_context = {'collection' : collection }, 
        **kwargs
    )

def painting_detail(request, slug, **kwargs):
    
    return list_detail.object_detail (
        request,
        queryset = Painting.objects.all(),
        slug = slug,
        template_object_name = "painting",
        **kwargs
    )

