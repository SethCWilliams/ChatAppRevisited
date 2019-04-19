
from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'api'

urlpatterns = [
    path('message/', views.MessageViewSet.as_view({
            'get': 'list',  # GET method should list objects
            'post': 'create',  # POST method should create object
        })),

    ]
