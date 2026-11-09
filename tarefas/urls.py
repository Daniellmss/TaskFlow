from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaInicial, name='pagina_inicial'),
    path('<int:id>/concluir/', views.concluirTarefa, name='concluir_tarefa'),
    path('<int:id>/editar/', views.editarTarefa, name='editar_tarefa'),
    path('<int:id>/excluir/', views.excluirTarefa, name='excluir_tarefa'),
]