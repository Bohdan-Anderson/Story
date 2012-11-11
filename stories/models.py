from django.db import models


class Story(models.Model):
  	name = models.CharField(max_length=100, editable=False)
  	data = models.CharField(max_length=100, editable=False)

	def __unicode__(self):
		return self.name

