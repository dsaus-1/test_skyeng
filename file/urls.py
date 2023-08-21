from django.urls import path

from file.apps import FileConfig
from file.views import FileListView, FileCreateView, FileUpdateView, FileDeleteView, page_logging


app_name = FileConfig.name


urlpatterns = [
    path('', FileListView.as_view(), name='home'),
    path('file_create/', FileCreateView.as_view(), name='file_create'),
    path('file_update/<str:pk>/', FileUpdateView.as_view(), name='file_update'),
    path('file_delete/<str:pk>/', FileDeleteView.as_view(), name='file_delete'),
    path('logging/', page_logging, name='logging')
]
