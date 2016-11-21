from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	# ex: /polls/
	url(r'^$', views.index, name='index'),
    	# ex: /polls/5/
    	url(r'^(?P<qString>.+)/$', views.game, name='game'),
    	# ex: /polls/5/results/
    	url(r'^results/$', views.results, name='results'),
]