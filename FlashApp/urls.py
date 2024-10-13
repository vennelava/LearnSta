from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcard_list, name='flashcard_list'),
    path('create/', views.create_flashcard, name='create_flashcard'),
     path('delete/<int:flash_id>/', views.delete_flashcard, name = 'delete_flashcard')
]
