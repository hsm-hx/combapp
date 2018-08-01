from django.urls import path

from . import views

app_name = 'equipments'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:equipment_id>/', views.detail, name='detail'),
  path('<int:equipment_id>/act/', views.act, name='act'),
  path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  ]
