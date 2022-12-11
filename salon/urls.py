from django.contrib import admin
from django.urls import path
from salon import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.home,name='home'),
    path('/about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('user_login',views.user_login,name='user_login'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_signup',views.admin_signup,name='admin_signup'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('user_home',views.user_home,name='user_home'),
    path('Logout', views.Logout, name='Logout'),




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)