from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
]