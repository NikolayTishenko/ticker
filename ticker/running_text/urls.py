from django.urls import path

from . import views

urlpatterns = [
    path('', views.generate_video),
    path('list/', views.get_list_text),
]
