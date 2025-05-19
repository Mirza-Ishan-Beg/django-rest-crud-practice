from django.urls import path
from .views import task_create, task_list, task_detail

urlpatterns = [
    path('task/', task_list),
    path('task/create', task_create),
    path('task/<int:pk>', task_detail),
]
