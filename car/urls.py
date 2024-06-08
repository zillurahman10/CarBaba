from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>/', views.DetailCarView.as_view(), name="details"),
    path('buy_car/<int:id>/', views.buy_car, name="buy_car"),
]