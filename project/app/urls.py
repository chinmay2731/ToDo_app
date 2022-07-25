from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('update_data/<str:pk>/',views.update_data,name='todo_update'),
    path('delete_data/<str:pk>/',views.delete_data,name='todo_delete'),
]