from django import template
from count.models import *

register = template.Library()

@register.inclusion_tag('count/list_stations.html')
def list_stations(cat_selected = 0):
    station = Station.objects.all()
    return {'station': station, "cat_selected": cat_selected}