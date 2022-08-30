from django.urls import path

from . import views

urlpatterns = [
    path("losses/", views.ListCreateLossView.as_view()),
    path("losses/<loss_id>/", views.RetrieveUpdateDestroyLossView.as_view()),
    path("losses/cpf/<cpf>/", views.ListCpfLossView.as_view()),
]
