from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'dbms'

urlpatterns = [
	path('', views.home, name='home'),
	path('check/', views.check, name='check'),
	path('update/<int:pk>/', views.update, name='update'),
	path('login/',auth_views.login, name='login'),
	path('logout/',auth_views.logout, name='logout'),
	path('award/<int:pk>/', views.award, name='award'),
	path('certify/', views.certify, name='certify'),
	path('chosevent/', views.chosevent, name='chosevent'),
	path('event/', views.event, name='event'),
]