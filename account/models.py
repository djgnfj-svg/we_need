from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser,
	PermissionsMixin)

# Create your models here.
# class Organization(TimeStampedModel):
# 	class Industries(models.TextChoices):
# 		PERSONAL = "personal"
# 		RETAIL = "retail"
# 		MANUFACTURING = "manufacturing"
# 		IT = "it"
# 		OTHERS = "others"
# 	name = models.CharField(max_length=50) # 회사이름
# 	industry = models.CharField(max_length=15, choices=Industries.choices,default=Industries.OTHERS)


class MyUserManager(BaseUserManager):
	def create_user(self, email, full_name, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		u = self.model(
			email=self.normalize_email(email),
			full_name=full_name,
		)
		u.set_password(password)
		u.save(using=self._db) #todo 정리
		return u

	def create_superuser(self, email, full_name, password):
		u = self.create_user(email=email,
							full_name=full_name,
							password=password,
							)
		u.is_admin = True
		u.save(using=self._db)
		return u

class MyUser(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email',
		max_length=255,
		unique=True,
	)
	nickname = models.CharField(
		verbose_name='nick_name',
		max_length=10,
		blank=False,
		unique=True,
		default='')

	date_of_birth = models.DateField()

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nick_name']

	def get_nick_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin


class UserProfile(models.Model):
	user = models.OneToOneField(
		MyUser,
		on_delete=models.CASCADE
	)
	nickname = models.CharField(null=False, max_length=30)
	profile_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True)