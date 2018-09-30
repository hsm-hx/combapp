from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:member_id>/', views.detail, name='detail'),
    path('<int:member_id>/results/', views.results, name='results'),
    path('<int:member_id>/vote/', views.vote, name='vote'),
]
