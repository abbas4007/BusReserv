from django.urls import path
from .views import Resveratin,Home

app_name='reserve'
urlpatterns=[
   path('register',Resveratin.as_view(),name='register'),
   path('home',Home.as_view(),name='home')

]