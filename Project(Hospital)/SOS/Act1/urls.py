from tkinter.font import names

from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('cat/',views.cat),
    path('login/',views.login,name='login'),
    path('forget/',views.forget,name='forget'),
    path('logout/',views.logout,name='logout'),
    path('menu/',views.circlepage1,name='menu'),
    path('appointment/',views.appoint,name='appointment')
]





