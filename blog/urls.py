from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.photo_list, name="gallery"),
    path('about/', views.about, name="about"),
    path('contact_ans/', views.contact_ans, name='contact_ans'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
