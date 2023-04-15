# map urls to the view functions

from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    # projects
    path('create/', views.create_view),
    path('list/', views.list_view),
    path('view/', views.project_selection),
    path('view/<id>/', views.detail_view),
    path('update/', views.project_selection),
    path('update/<id>/', views.update_view),
    path('delete/', views.project_selection),
    path('delete/<id>/', views.delete_view),
    # tasks
    path('new/', views.new_view),
    path('bullet/', views.bullet_view),
    path('edit/', views.task_selection),
    path('edit/<id>/', views.edit_view),
    path('remove/', views.task_selection),
    path('remove/<id>/', views.remove_view),
    # homepage
    path('', views.home),
    # success page
    path('success/', views.success_view)
]