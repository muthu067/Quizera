from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
    path("home/",views.home,name='home'),
    path("contact/",views.contact,name="contact"),
    path("pages/<str:slug>/",views.detail,name="detail"),
    path("new_url",views.new_url,name='new_url'),
    path("old_url",views.old_url,name="old_url"),
    path("",views.login,name="login"),
    path("about/",views.about,name='about'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout')
]


 