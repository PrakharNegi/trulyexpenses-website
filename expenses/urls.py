from audioop import add
from django.urls import URLPattern


from django.urls import path
from . import views







urlpatterns = [
    path('',views.index,name="expenses"),
    path('add-expense',views.add_expense,name="add-expense"),


]