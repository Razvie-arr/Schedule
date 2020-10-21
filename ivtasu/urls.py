from django.urls import path
from . import views

urlpatterns = [
    path('', views.zan_list, name='zan_list'),
    path('<int:id>', views.zan_list, name='zan_edit'),
    path('raspisanie', views.raspis, name='raspis'),
    path('raspisanie/<int:id>', views.raspis_edit, name='raspis_edit'),
    path('raspisanie_delete/<int:id>', views.raspis_delete, name='raspis_delete'),
]