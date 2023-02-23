from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.projects, name='projects'),
    # path can change as long as name stays the say it wont disconnect in other files
    path('project/<str:pk>', views.project, name='project') 
]