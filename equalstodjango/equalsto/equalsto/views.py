from __future__ import absolute_import
from django.views import generic

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .forms import RegistrationForm, LoginForm

from django.contrib.auth.models import User

from braces import views

class HomePageView(generic.TemplateView):
	template_name = 'home.html'

class SignUpView(generic.CreateView):
	form_class = RegistrationForm
	success_url = reverse_lazy('home')
	model = User
	template_name = 'accounts/signup.html'
	views.AnonymousRequiredMixin
	views.FormValidMessageMixin
	form_valid_message = 'you logged in'


class LogOutView(generic.RedirectView):
	url = reverse_lazy('home')
	views.LoginRequiredMixin
	views.MessageMixin

	def get(self, request, *args, **kwargs):
		logout(request)
		#self.messages.success("You've been logged out. Come back soon!")
		return super(LogOutView, self).get(request, *args, **kwargs)

class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'
    views.AnonymousRequiredMixin
    views.FormValidMessageMixin
    form_valid_message = 'you logged in'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)