from __future__ import absolute_import
from django.http import HttpResponse
from django.template import loader

from .models import Question



#apparently we can use render() as a shortcut instead of httpresponse. https://docs.djangoproject.com/en/1.10/intro/tutorial03/
#for more information

#display the template at polls/templates/polls/index.html
def index(request):
    latest_question_list = Question.objects.order_by('-question_String')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#display data for each question
def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." %question_id)

