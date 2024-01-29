from django.urls import path
from . import views
from .views import Post_List

app_name = 'news'

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path("", views.Post_List.as_view(), name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/",
         views.post_detail, name="post_detail"),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
]
