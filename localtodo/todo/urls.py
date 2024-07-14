from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.ToDoListView.as_view(), name='todo-list'),
    path('new/', views.CreateToDoView, name='create'),
    path('<int:pk>/edit', views.Update, name='edit'),
    path('<int:pk>/delete', views.Delete, name='delete'),
]
