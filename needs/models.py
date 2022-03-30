from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User as U
# Create your models here.

class TimeStampedModel(models.Model):
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

# 카테고리가 있는 이유 -> 일단 분류를 하기 위해서인데 그러면 그걸 구지 카테고리로 하는 이유는??
# 운영자 쪽에서 니즈의 분류를 파악하고 그부분을 추가해서 운영자 쪽에서 이상한 테그가 유행하는걸 방지할 수 있고
# 생각해보니 이러면 운영자쪽에서 추가를 어케하니...?

class Categories(models.Model):
	category_name = models.CharField(max_length=20, validators=[MinValueValidator(2)])

class Needs(TimeStampedModel):

	title = models.CharField(max_length=20, null=False)
	description = models.TextField(null=True)
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
	# categorys = models.CharField(
	# 	max_length=30,
	# 	choices=Categorys.choices,
	# 	default=Categorys.ETC,
	# )
	creator = models.ForeignKey(U,on_delete=models.CASCADE,null=True, related_name="creator")
	like = models.ManyToManyField(U, null=True)
	like_count = models.PositiveIntegerField(default=0)

	def __str__(self):
			return self.title

class Comment(TimeStampedModel):
	need = models.ForeignKey(Needs, on_delete=models.CASCADE)
	writer = models.ForeignKey(U,on_delete=models.CASCADE,null=False)
	parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

	content = models.CharField(max_length=300)

	class Meta:
		db_table = 'comments'