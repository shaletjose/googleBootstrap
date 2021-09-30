from django.urls import path
from googleBootstrapApp import views
app_name='googleapp'
urlpatterns = [
    path('', views.index, name='index'),

]