from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('home',views.index,name="home"),
    path('career',views.career,name="career"),
    path('contact',views.contact,name="contact"),
    path('application',views.application,name="application")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
