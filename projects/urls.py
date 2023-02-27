from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.projects, name='projects'),
    # path can change as long as name stays the say it wont disconnect in other files
    path('project/<str:pk>', views.project, name='project'),
    path('create-project/', views.createProject, name='create-project'),
    path('update-project/<str:pk>/', views.updateProject, name='update-project'),
]