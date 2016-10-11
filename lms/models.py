from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	isTeacher = models.BooleanField(default='False')
	isStudent = models.BooleanField(default='False')
	isResearcher = models.BooleanField(default='False')
	isOther = models.BooleanField(default='True')
	has_IRB_release = models.BooleanField(default='False')	
	age = models.IntegerField(blank=True, null=True)
	race = models.CharField(max_length=20, blank=True, null=True)
	gender = models.CharField(max_length=10, blank=True, null=True)
	#picture = models.ImageField(upload_to='profile_images', blank=True)

	
	
	def __str__(self):
		return "%s's profile" % self.user
		
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)
		

post_save.connect(create_user_profile, sender=User)

class Project(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=30)
	isPublic = models.BooleanField(default=False, verbose_name="Public?")
	isApproved = models.BooleanField(default=False, verbose_name="Approved?")

	def __str__(self):
		return "%s's project" % self.owner
		
class Lesson(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=30)
	isPublic = models.BooleanField(default=False, verbose_name="Public?")

	def __str__(self):
		return "%s's lesson" % self.owner
		
class Test(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=30)
	isPublic = models.BooleanField(default=False, verbose_name="Public?")

	def __str__(self):
		return "%s's lesson" % self.owner