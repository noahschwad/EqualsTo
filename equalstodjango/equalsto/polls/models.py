

from django.db import models

#import user data model
from django.contrib.auth.models import User

#import these two so we can dynamically update our users table with current users
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Question(models.Model):
	question_String = models.CharField(max_length=200)
	answer_1 = models.CharField(max_length=200)
	answer_2 = models.CharField(max_length=200)

"""
#onetoone field of users that makes sure there are no return errors when creating user attribute table
class tempUser(AbstractUser):
	def customer_profile(self):
		try:
			return self._customer_profile
		except CustomerProfile.DoesNotExist:
			return CustomerProfile.objects.create(user=self,)


class UserAttributes(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	"""

class Answer(models.Model):
	#connect answer to question
	#question = models.ForeignKey(Question, on_delete=models.CASCADE)
	#connect answer to user
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#data holding quiz answers
	answer_1 = models.IntegerField(default = 0)
	answer_2 = models.IntegerField(default = 0)
	answer_3 = models.IntegerField(default = 0)
	answer_4 = models.IntegerField(default = 0)
	answer_5 = models.IntegerField(default = 0)
	answer_6 = models.IntegerField(default = 0)
	answer_7 = models.IntegerField(default = 0)
	answer_8 = models.IntegerField(default = 0)
	answer_9 = models.IntegerField(default = 0)
	answer_10 = models.IntegerField(default = 0)

"""Noah S was adding onetoonefield from user to answer,
in addition I had to migrate the DB because changing models
changes the db. got back to "no url to direct to" error which zack 
had fixed and I just hadnt gotten off of github yet. should work but
might need to rebuild database so answers instance gets created
correctly for every user :)
"""

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Answer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.answer.save()
	
	#answer_text = models.CharField(max_length=200)
	#votes = models.IntegerField(default=0)
	

#create table that will mirror django's built in user table
#attach additional attributes here.


