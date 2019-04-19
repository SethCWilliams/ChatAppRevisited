from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Message


class HomeView(TemplateView):
    template_name = 'chat/index.html'
# Need to make a 'home.html' for the home.view


# @login_required(login_url='/accounts/login/')
class ChatIndexView(TemplateView):
    template_name = 'chat/chat.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ChatIndexView, self).dispatch(request, *args, **kwargs)
