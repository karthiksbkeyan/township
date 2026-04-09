from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice_list, name='home'),
    path('create-admin/', views.create_admin),
]