import datetime
from django import template

register = template.Library()

@register.filter(name="get_age")
def get_age(value):
    today = datetime.date.today()
    return today.year - value.year - ((today.month, today.day) < (value.month, value.day))