from django.urls import path
from . import views
from .api import views as api

urlpatterns = [
    path('', views.index, name='data_portal'),


    #api
    path('api/topic-lists', api.topic_lists),
    path('api/category-with-indicator/<str:id>', api.category_with_indicator),
]