from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('topic/', topic, name='topic'),
    path('delete_topic/<int:id>', delete_topic, name='delete_topic'),
    path('edit_topic/', edit_topic, name='edit_topic'),

    #Category
    path('categories/', categories, name='categories'),
    path('edit_category/', update_category, name='update_category'),
    path('delete_category/<str:id>', delete_category, name='delete_category'),

    #Indicator
    path('indicators/<str:id>', indicators, name='indicators'),

]