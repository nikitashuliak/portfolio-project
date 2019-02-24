from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
