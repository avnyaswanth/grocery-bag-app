from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('add/',views.add_view,name="add"),
    path('update/<int:id_num>',views.update_view,name="update"),
    path('delete/<int:id_num>',views.delete_view,name="delete"),
]