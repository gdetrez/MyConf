from django import template

register = template.Library()

@register.inclusion_tag('embedded_map.djhtml')
def map(lat, long, style=""):
    return {
        'lat': float(lat),
        'long': float(long),
        'style': style,
}   
