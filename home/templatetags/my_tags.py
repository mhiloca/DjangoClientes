from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag
def the_time(format_string):
    return datetime.now().strftime(format_string)


@register.simple_tag
def footer_msg():
    return 'desenvolvimento django 2.bolinhas'

