from django.db import models
# Create your models here.

class TimeStampedModel(models.Model):
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

# 카테고리가 있는 이유 -> 일단 분류를 하기 위해서인데 그러면 그걸 구지 카테고리로 하는 이유는??
# 운영자 쪽에서 니즈의 분류를 파악하고 그부분을 추가해서 운영자 쪽에서 이상한 테그가 유행하는걸 방지할 수 있고
# 
class Categotise(TimeStampedModel):
	Category_name = models.CharField(max_length=10, null=False)


class Needs(TimeStampedModel):
	main_img = models.ImageField(upload_to="image")
	title = models.CharField(max_length=20, null=False)
	description = models.TextField(null=False)
	category = models.ForeignKey(Categotise, on_delete=models.CASCADE)

	# slug = models.SlugField(unique=True, max_length=20)
	# tags = TaggableManager()

	def __str__(self):
			return self.title
