from django.contrib import admin
from gallery.models import *

class ItemAttributeInLine(admin.TabularInline):
    model=ItemAttribute

admin.site.register(Attribute)

class PaintingAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        ItemAttributeInLine,
    ]
    
admin.site.register(Painting, PaintingAdmin)

class CollectionAdmin(admin.ModelAdmin) :
   prepopulated_fields = {"slug": ("title",)}
   filter_horizontal = ('paintings',)
admin.site.register(Collection, CollectionAdmin)


