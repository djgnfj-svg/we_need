from django import template
from needs.models import Categories

register = template.Library()

#특정 템플릿과 결합해서 사용
@register.inclusion_tag("search_bar.html", takes_context=True)
def redner_serach_bar(context):
	return{
		"selected_category" : context.get('selected_category'),
		"selected_keyword" : context.get('selected_keyword', ' '),
		"fetched_categories" : Categories.objects.all()
	}
