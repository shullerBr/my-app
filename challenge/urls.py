from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'challenge'

urlpatterns = [
    #url(r'^', views.challenge_list, name='challenge_list'),
    #url(r'^<pk>/$', views.challenge_detail, name='challenge_detail'),
    #url(r'^create/$', views.challenge_create, name='challenge_create'),
    path('', views.challenge_list, name='challenge_list'),
    path('create/', views.challenge_create, name='challenge_create'),
    path('challenge/<int:pk>/', views.challenge_detail, name='challenge_detail'),
    path('challenge/<int:pk>/edit/', views.challenge_edit, name='challenge_edit'),
    #url('<int:pk>/', views.challenge_detail, name='challenge_detail'),
    #url(r'challenge/(?P<pk>\d+)/$',views.challenge_detail,name="challenge_detail"),
    #url('challenge/<int:pk>/', views.challenge_detail, name='challenge_detail'),
    #path('new/', views.challenge_new, name='challenge_new'),
    #path('new/', views.challenge_new, name='challenge_new'),
]
