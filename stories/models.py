from django.db import models
from django.contrib.auth.models import User

from story.settings import SITE_ROOT\

class Story(models.Model):
	creator = models.ForeignKey(User)	
  	name = models.CharField(max_length=100)
  	data = ""

	def __unicode__(self):
		return self.name

