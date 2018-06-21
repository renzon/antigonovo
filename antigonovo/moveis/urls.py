from django.urls import path

from antigonovo.moveis import views

app_name = 'moveis'
urlpatterns = [
    path('', views.index, name='index'),
]
