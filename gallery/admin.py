from django.contrib import admin
from gallery.models import Painting, Collection, Attribute

class PaintingAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Painting, PaintingAdmin)

class CollectionAdmin(admin.ModelAdmin) :
   prepopulated_fields = {"slug": ("title",)}
   filter_horizontal = ('paintings',)
admin.site.register(Collection, CollectionAdmin)

admin.site.register(Attribute)
