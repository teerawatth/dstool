from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('search/',s,name='s'),
    path('edit/course/<int:id>/',edit,name='edit'),
    path('d/',delete_page,name='d'),
    path('delete/',delete,name='delete'),
]