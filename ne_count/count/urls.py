from django.urls import path
from .views import *

urlpatterns = [
    path('', Explorer.as_view(), name='home'),
    path('add_parameters/', AddParamrters.as_view(), name='add_parameters'),
    path('station/<int:station_id>', ShowEngine, name='station'),
    path('journal/', JournalView.as_view(), name='journal' ),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]