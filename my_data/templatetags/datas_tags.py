from django import template
from ..models import My_data,Classification,Tag_name
register = template.Library()

@register.simple_tag
def get_recent_data(num = 5):
    return My_data.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_popular_data(num = 5):
    return My_data.objects.all().order_by('-visiting')[:num]

@register.simple_tag
def get_classification():
    return Classification.objects.all()



@register.simple_tag
def get_tags():
    return Tag_name.objects.all()

@register.simple_tag
def get_whole_content(num = 20):
    return My_data.objects.all().order_by('tags')[:num]


@register.simple_tag
def get_whole_categ(num = 10):
    return My_data.objects.all().order_by('category')[:num]