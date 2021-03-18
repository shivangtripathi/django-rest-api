from django.urls import path

from . import views

urlpatterns = [
    path('',views.ApiOverview,name="api-overview"),
    path('task-list/',views.todosList,name="task-list"),
    path('task-detail/<str:pk>/',views.todosDetail,name="task-detail"),
    path('task-update/<str:pk>/',views.todosUpdate,name="task-update"),
     path('task-delete/<str:pk>/',views.todosDelete,name="task-delete"),
    path('task-create/',views.todosAdd,name="task-create"),
]
