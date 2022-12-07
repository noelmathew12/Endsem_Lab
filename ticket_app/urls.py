from django.urls import path
from . import views
app_name = 'todo_project'
urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.flightbooking, name='booking' ),
    path('book/', views.booking_view , name='booking1' ),
]