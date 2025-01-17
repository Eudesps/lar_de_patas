from django.urls import path
from .views import listar_animais, adicionar_animal, atualizar_animal, detalhes_animal, excluir_animal

urlpatterns = [
    path('animais/', listar_animais, name='listar_animais'),
    path('animal/adicionar/', adicionar_animal, name='adicionar_animal'),
    path('animal/editar/<int:pk>/', atualizar_animal, name='atualizar_animal'),
    path('animal/detalhes/<int:pk>/', detalhes_animal, name='detalhes_animal'),
    path('animal/excluir/<int:pk>/', excluir_animal, name='excluir_animal')
 ]