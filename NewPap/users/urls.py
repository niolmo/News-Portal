from django.urls import path
from . import views
# from .views import

app_name = 'news'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
