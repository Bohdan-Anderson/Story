from django.http import HttpResponse
from settings import SITE_ROOT\

from django.utils import simplejson
import json

from django import forms

from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.utils import simplejson

def hello(request):
    words = "text goes in here"
    return HttpResponse("Hello world")

def loadData():
	jd = open(SITE_ROOT + '\..\data\data.json')
	
	jjd = simplejson.load(jd)
	return jjd


def check_keys(jd):
    stuff = []
    for z in range(len(jd)):
        KEY = str(z)
        for k in jd[KEY].iterkeys():
            if not k in stuff: stuff.append(k)
    return stuff



class ContactForm(forms.Form):
    title = forms.CharField()
    intro = forms.CharField()
    conclusion = forms.CharField()


def viewData(request):
	temp = loadData()
	return HttpResponse(temp[1][4])

def editData(request):
	json_data = loadData()
	myFormList = []
	for a in range(len(json_data)):
		myForm = ContactForm({'title':json_data[a][1], 'intro':json_data[a][3], 'conclusion':json_data[a][5]})
		myFormList.append(myForm)
	print SITE_ROOT
	return render_to_response('table.html', {'data':myFormList})

def playGame(request):
	jd = open(SITE_ROOT + '\..\data\data.json')
	jjd = simplejson.load(jd)

	return render_to_response('story.html',{'data':jjd})
