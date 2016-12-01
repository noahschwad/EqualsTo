from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	# ex: /polls/
	url(r'^$', views.index, name='index'),
    	# ex: /polls/5/
    	url(r'^(?P<qNum>[0-9]+)/$', views.game, name='game'),
	url(r'^(?P<qNum>[0-9]+)/answered1/$', views.answered1, name='answered1'),
	url(r'^(?P<qNum>[0-9]+)/answered2/$', views.answered2, name='answered2'),
    	url(r'^results/$', views.results, name='results'),
]