from django.urls import path
from . import views

urlpatterns = [
    # ...other URL patterns...
    path('login/', views.login_view, name='login'),
]
