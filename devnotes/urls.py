from django.urls import path

from . import views
app_name = 'devnotes'
urlpatterns = [
    path('', views.index, name='index'),
    path('update-status/', views.UpdateStatus, name='update-status'),
    path('add-note/', views.add, name='add-note'),
]
