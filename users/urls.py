from django.urls import path

from . import views

app_name = 'equipments'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:equipment_id>/', views.detail, name='detail'),
  path('<int:equipment_id>/act/', views.act, name='act'),
  #path('<int:equipment_id>/borrowing/', views.borrowing, name='borrowing'),
  #path('<int:equipment_id>/borrow_act/', views.borrow_act, name='borrow_act'),
  #path('<int:equipment_id>/returning/', views.returning, name='returning'),
  #path('<int:equipment_id>/return_act/', views.return_act, name='return_act'),
  #path('<int:equipment_id>/extension/', views.extension, name='extension'), 
  #path('<int:equipment_id>/extend_act/', views.extend_act, name='extend_act'),
  ]
