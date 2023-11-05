from django.urls import path
from . import views

urlpatterns = [
    path('generer_code_qr/<int:id_agent>/', views.generate_qr, name='generate_qr'),
    path('dechiffrer/', views.dechiffrer, name='dechiffrer'),
]