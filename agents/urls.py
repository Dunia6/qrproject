from django.urls import path
from . import views


urlpatterns = [
    path('ajouter_agent/', views.addAgent, name='addagent'),
    path('agent/<int:id>/', views.agentView, name='agent'),
]
