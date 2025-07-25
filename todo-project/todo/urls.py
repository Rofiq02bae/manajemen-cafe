from django.urls import path

from .views import index_view, detail_view, create_view, update_view

app_name = 'todo'
urlpatterns = [
    path('', index_view, name='index'),
    path('<int:task_id>/', detail_view, name='detail'),
    path('create/', create_view, name='create'),
    path('update/<int:task_id>/', update_view, name='update'),
]