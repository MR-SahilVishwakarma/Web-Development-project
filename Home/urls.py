from django.contrib import admin
from django.urls import path
from Home import views

admin.site.site_header = "SuperTaxi Admin"
admin.site.site_title = "SuperTaxi Admin Portal"
admin.site.index_title = "Welcome to SuperTaxi Researcher Portal"

urlpatterns = [
    # path('', views.index , name='Home'),
    path('', views.index , name='home'),
    path('contact/', views.contact , name='contact'),
    path('saveContact/', views.saveContact , name='saveContact'),
    path('about/', views.about , name='about'),
    path('services/', views.services , name='services'),
    path('taxefare/', views.taxifare , name='taxifare'),
    path('bill/', views.bill , name='bill'),
    path('savebill/', views.savebill , name='savebill'),
    path('login/', views.login , name='login'),
    path('signin/', views.signin , name='signin'),
    path('saveSignin/', views.saveSignin , name='saveSignin'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('val_login/', views.val_login , name='val_login'),
    path('logout/', views.logout , name='logout'),
]