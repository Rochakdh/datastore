from django.urls import path
from .views import Index,TableView,ProfileCreate,ProfileDelete,ProfileUpdate

app_name = 'crud'

urlpatterns = [
    path('',Index.as_view(),name='home'),
    path('detail',TableView.as_view(),name='table'),
    path('create',ProfileCreate.as_view(),name = 'create'),
    path('delete/<int:pk>/',ProfileDelete.as_view(),name = 'delete'),
    path('update/<int:pk>/',ProfileUpdate.as_view(),name = 'update'),
]