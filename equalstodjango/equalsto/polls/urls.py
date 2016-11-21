from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	# ex: /polls/
	url(r'^$', views.index, name='index'),
    	# ex: /polls/5/
    	url(r'^(?P<question_id>[0-9]+)/$', views.game, name='game'),
    	# ex: /polls/5/results/
    	url(r'^results/$', views.results, name='results'),
]