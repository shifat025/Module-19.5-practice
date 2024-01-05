from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.add_album, name='post'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]