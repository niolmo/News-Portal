from django.urls import path
from . import views
# from .views import

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
