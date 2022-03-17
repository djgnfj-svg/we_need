from django import template
from django.utils.html import mark_safe

from datetime import time, datetime, date, timedelta

register = template.Library()

@register.filter(name="category_name")
def category_neme(value):
	temp = ["etc","Politics","Society","person","individual"]
	if value in temp:
		if value == "etc":
			return "기타"
		elif value == "Politics":
			return "정치"
		elif value == "Society":
			return "사회"
		elif value == "person":
			return "사람"
		elif value == "individual":
			return "개인"
	return "오류"