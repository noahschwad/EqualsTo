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
	user_list = Answer.objects.all() #list of answers to compare
	currentUser = get_object_or_404(Answer, user = request.user) #find currently logged in user
	tempRelativeScore = 0
	highestScore = 0
	highestScoreUser = 0
	for x in range(len(user_list)):
		print (user_list[x])
		if (currentUser.answer_1 == user_list[x].answer_1):
			tempRelativeScore += 1
		if (currentUser.answer_2 == user_list[x].answer_2):
			tempRelativeScore += 1
		if (currentUser.answer_3 == user_list[x].answer_3):
			tempRelativeScore += 1
		if (currentUser.answer_4 == user_list[x].answer_4):
			tempRelativeScore += 1
		if (currentUser.answer_5 == user_list[x].answer_5):
			tempRelativeScore += 1
		if (currentUser.answer_6 == user_list[x].answer_6):
			tempRelativeScore += 1
		if (currentUser.answer_7 == user_list[x].answer_7):
			tempRelativeScore += 1
		if (currentUser.answer_8 == user_list[x].answer_8):
			tempRelativeScore += 1
		if (currentUser.answer_9 == user_list[x].answer_9):
			tempRelativeScore += 1
		if (currentUser.answer_10 == user_list[x].answer_10):
			tempRelativeScore += 1
		if (highestScore > tempRelativeScore):
			highestScore = tempRelativeScore
			highestScoreUser = x
	match = user_list[highestScoreUser].user
	#print out highestScoreUser
	return render(request, 'polls/results.html',{ "match_List": match })

