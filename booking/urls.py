#bookingbite/booking/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('week/', views.get_week_dishes, name='week_dishes'),
    path('add-attendance/', views.add_attendance, name='add_attendance'),
    path('remove-attendance/', views.remove_attendance, name='remove_attendance'),
    # path('week/', views.get_week_dishes, name='week'),
    # path('week/<int:week>/', views.get_week_dishes, name='week_id'),
]
