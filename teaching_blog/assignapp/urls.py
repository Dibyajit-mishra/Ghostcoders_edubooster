from django.urls import path
from assignapp import views

urlpatterns = [
    path('',views.add_show,name ='add'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('<int:id>/', views.update_data, name='update'),
]