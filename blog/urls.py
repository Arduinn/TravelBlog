from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name="contact"),
    path('contact_ans/', views.contact_ans, name="contact_ans"),
    path('posts/', views.posts_list, name='posts_list'),
]
