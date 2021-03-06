from django.conf.urls import url
from django.urls import path
from . import views



app_name = 'test_db_app'

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    path("<str:productId>", views.detail, name="detail"),
    path("<str:productId>/favorite", views.favorite, name="favorite"),
]
