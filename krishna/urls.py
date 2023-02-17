from django.urls import path 

from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('yashoda',views.yashoda,name='yashoda'),
]