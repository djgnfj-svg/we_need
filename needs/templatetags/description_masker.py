from django import template
from django.utils.html import mark_safe

from datetime import time, datetime, date, timedelta

register = template.Library()

@register.filter(name="DM")
def desciption_masker(value):
	temp = value[:20]
	if 20 < len(value):
		temp = temp + "..."
	return temp