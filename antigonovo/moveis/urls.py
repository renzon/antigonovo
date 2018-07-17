from django.urls import path

from antigonovo.moveis import views

app_name = 'moveis'
urlpatterns = [
    path('', views.index, name='index'),
    path('novo', views.new, name='new'),
    path('criar', views.create, name='create'),
]
