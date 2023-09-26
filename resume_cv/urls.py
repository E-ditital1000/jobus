# resume_cv/urls.py
from django.urls import path
from . import views

app_name = 'resume_cv'

urlpatterns = [
    path('create/', views.create_cv, name='create_cv'),
    path('list/', views.cv_list, name='cv_list'),
    path('download/<int:cv_id>/', views.download_cv, name='download_cv'),
]
