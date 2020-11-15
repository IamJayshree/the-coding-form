from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:module_id>',views.module,name='module'),
]
