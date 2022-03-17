from django.db import models
from account.models import MyUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class TimeStampedModel(models.Model):
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

# 카테고리가 있는 이유 -> 일단 분류를 하기 위해서인데 그러면 그걸 구지 카테고리로 하는 이유는??
# 운영자 쪽에서 니즈의 분류를 파악하고 그부분을 추가해서 운영자 쪽에서 이상한 테그가 유행하는걸 방지할 수 있고
# 

class Needs(TimeStampedModel):
	class Categorys(models.TextChoices):
		POLITICS = "Politics", _("정치")
		SOCIETY = "Society", _("사회") 
		PERSON = "person", _("사람") 
		INDIVIDAUL = "individual", _("개인") 
		ETC = "etc", _("기타") 

	title = models.CharField(max_length=20, null=False)
	description = models.TextField(null=True)
	categorys = models.CharField(
		max_length=30,
		choices=Categorys.choices,
		default=Categorys.ETC,
	)
	creator = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True, related_name="creator")
	like = models.ManyToManyField(MyUser, null=True,related_name="like")
	like_count = models.PositiveIntegerField(default=0)

	def __str__(self):
			return self.title

class Comment(TimeStampedModel):
	need = models.ForeignKey(Needs, on_delete=models.CASCADE)
	writer = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=False)
	parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

	content = models.CharField(max_length=300)

	class Meta:
		db_table = 'comments'