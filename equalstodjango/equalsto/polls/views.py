from __future__ import absolute_import
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question
from .models import Answer


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
def game(request, qNum):
	currentQuestion = Question.objects.get(id = qNum)
	context = {
		'question': currentQuestion,
	}
	return render(request, 'polls/game.html', context)

def answered1(request, qNum):
	currentAnswer = get_object_or_404(Answer, user = request.user)
	whichAnswer = "answer_"+str(qNum)
	setattr(currentAnswer, whichAnswer, 1)
	currentAnswer.save()
	return HttpResponseRedirect(reverse('polls:index'))

def answered2(request, qNum):
	currentAnswer = get_object_or_404(Answer, user = request.user)
	whichAnswer = "answer_"+str(qNum)
	setattr(currentAnswer, whichAnswer, 2)
	currentAnswer.save()
	return HttpResponseRedirect(reverse('polls:index'))

def results(request):
	context = {}
	return render(request, 'polls/results.html', context)

