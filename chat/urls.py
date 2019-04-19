from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('chat/', views.ChatIndexView.as_view(), name='chat'),
    # path('create/', views..as_view(), name=''),
    # path('update/<int:pk>/', views..as_view(), name='')
    ]
