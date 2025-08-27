from django import template
from django.utils.text import slugify
register = template.Library()

@register.filter(name='create_slug')
def create_slug(data,arg):
    if hasattr(data,arg):
        string_name = slugify(getattr(data, arg).lower().replace(' ı', 'i').replace('ü', 'u').replace('ö', 'o'))
        return f"{string_name}"
    else:
        return f"Belirtilen özellik '{arg}' bulunamadı."
    
@register.filter(name='get_path_part')
def get_path_part(value,arg):
    return value.split('/')[arg] 
    