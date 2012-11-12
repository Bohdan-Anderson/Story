from django.http import HttpResponse, HttpResponseRedirect
from settings import SITE_ROOT\

from django.utils import simplejson
import json, datetime

from django import forms

from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.utils import simplejson

from django.core.files import File

from django.core.context_processors import csrf


###################################
#Game play
###################################
def loadData():
	jd = open(SITE_ROOT + '\..\data\data.json')
	jjd = simplejson.load(jd)

	return jjd

def playGame(request):
	##reciving end of jquery ajax
	if request.method == 'GET':
		GET = request.GET
		if GET.has_key(u'data'):
			myFile = open(SITE_ROOT + '\..\data\writtingData.txt', 'a')	

			data = GET[u'data']
			scene = GET[u'scene']
			time = datetime.datetime.now().strftime("{'year':%Y, 'month':%m,'day':%d, 'hour':%H, 'miute':%M, 'second':%S}")

			myFile.write( data + " " + scene + " " + time + " \n")	
			myFile.close()

	jd = open(SITE_ROOT + '\..\data\data.json')
	jjd = simplejson.load(jd)

	return render_to_response('story.html',{'data':jjd })#,'csrf_token': c})


###################################
#Creating game options
###################################
from stories.models import Story

def viewUsersStories(request):
	if request.user.is_authenticated():
		print request.user

		stories = Story.objects.filter(creator=request.user)
		title = "%s's Stories" % request.user
		body = ""
		length = len(stories)
		if length == 0:
			body = "no Stories"
		else:
			for i in range(len(stories)):
				body += stories[i].name	


		return render_to_response("base.html", {'title':title, 'body': body })
	else:
		return HttpResponseRedirect('/login/')



def createStory(request):
	if request.user.is_authenticated():
		c = {'title':"Create Story"}
		c.update(csrf(request))

		if request.method == "POST":
			POST = request.POST
			name = POST[u'storyName']
			newStory = Story(name = name , creator = request.user)
			newStory.save()	
			return HttpResponseRedirect("/objectView/")
		return render_to_response("createStory.html", c)
	else:
		return HttpResponseRedirect('/login/')

###################################
#editing the data possibly
###################################

class ContactForm(forms.Form):
    title = forms.CharField()
    intro = forms.CharField()
    conclusion = forms.CharField()

def editData(request):
	json_data = loadData()
	myFormList = []
	for a in range(len(json_data)):
		myForm = ContactForm({'title':json_data[a][1], 'intro':json_data[a][2], 'conclusion':json_data[a][4]})
		myFormList.append(myForm)
	#print SITE_ROOT
	return render_to_response('table.html', {'data':myFormList})