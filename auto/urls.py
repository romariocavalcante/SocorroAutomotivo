from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("solicitar-socorro/", views.solicitar_socorro, name="solicitar_socorro"),
    path("socorrista-encontrado/", views.socorrista_encontrado, name="socorrista_encontrado"),
    path("guincho/", views.guincho, name="guincho"),
    path("troca-pneu/", views.troca_pneu, name="troca_pneu"),
    path("chaveiro-automotivo/", views.chaveiro_automotivo, name="chaveiro_automotivo"),
    path("recarga-bateria/", views.recarga_bateria, name="recarga_bateria"),
    path("pane-mecanica/", views.pane_mecanica, name="pane_mecanica"),
    path("falta-combustivel/", views.falta_combustivel, name="falta_combustivel"),
    path("solicitar-guincho/", views.solicitar_guincho, name="solicitar_guincho"),
    path("solicitar-troca-pneu/", views.solicitar_troca_pneu, name="solicitar_troca_pneu"),
    path("solicitar-chaveiro-automotivo/", views.solicitar_chaveiro_automotivo, name="solicitar_chaveiro_automotivo"),
    path("solicitar-recarga-bateria/", views.solicitar_recarga_bateria, name="solicitar_recarga_bateria"),
    path("solicitar-pane-mecanica/", views.solicitar_pane_mecanica, name="solicitar_pane_mecanica"),
    path("solicitar-falta-combustivel/", views.solicitar_falta_combustivel, name="solicitar_falta_combustivel"),
]