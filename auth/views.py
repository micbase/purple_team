
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import (
    View,
    FormView,
)

from auth.forms import (
    LoginForm,
    RegisterForm,
)


class AuthView(FormView):
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(AuthView, self).form_valid(form)


class LoginView(AuthView):
    template_name = 'dashboard/login.html'
    form_class = LoginForm


class RegisterView(AuthView):
    template_name = 'dashboard/register.html'
    form_class = RegisterForm


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
