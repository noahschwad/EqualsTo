from __future__ import absolute_import
from django.shortcuts import render
from django.template import loader

from .models import Question



#apparently we can use render() as a shortcut instead of httpresponse. https://docs.djangoproject.com/en/1.10/intro/tutorial03/
#for more information

#display the template at polls/templates/polls/index.html
def index(request):
    	latest_question_list = Question.objects.order_by('-question_String')[:5]
    	context = {
        	'latest_question_list': latest_question_list,
    	}
    	return render(request, 'polls/index.html', context)

#play game
def game(request, qString):
	currentQuestion = Question.objects.get(question_String = qString)
	context = {
		'question': currentQuestion,
	}
	return render(request, 'polls/game.html', context)

def results(request):
	context = {}
	return render(request, 'polls/results.html', context)

