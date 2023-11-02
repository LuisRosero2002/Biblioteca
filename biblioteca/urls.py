"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autores/', views.AutoresListView.as_view(), name='autores-list'),

    # path('selection/<int:pk>/detail/',
    #      views.SelectionDetailView.as_view(), name='selection-detail'),
    path('libro/', views.LibroListView.as_view(), name='libro-list'),
    
    # path('player/<int:pk>/detail/',
    #      views.PlayerDetailView.as_view(), name='player-detail'),

    # Update
    path('autores/<int:pk>/update/',views.AutoresUpdate.as_view(),name='autores-update'), 
    path('libro/<int:pk>/update/',views.LibroUpdate.as_view(),name='libro-update'), 
    
    #Create
    path('autores/create/', views.AutorCreate.as_view(), name='autores-create'),
    path('libro/create/', views.LibroCreate.as_view(), name='libro-create'),

    #Delete
    path('autores/<int:pk>/delete/', views.AutoresDelete.as_view(), name='autores-delete'),
    path('libro/<int:pk>/delete/', views.LibroDelete.as_view(), name='libro-delete'),

]
