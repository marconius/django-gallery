from django import template
from gallery.models import Painting

register = template.Library()

#i n the works

''' 

@register.tag
def random_painting(parser, token) :
    
    # bits = token.split_contents()[1:]
    #if len(bits) >= 1:
    #    raise template.TemplateSyntaxError, "%r tag does not accept any arguments" % token.contents.split()[0]
    number = 1;
    painting = Painting.objects.filter(id=number)
    if painting.exists() :
        painting_list = painting.all 
        
    return painting_list
        
'''    

