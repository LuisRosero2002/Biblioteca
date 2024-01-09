from django.contrib import admin
from django.urls import path
from libros.views import LibrosViews ,AutoresListView, obtener_autores, obtener_generos,obtener_paises,AutoresUpdate,LibroUpdate,actualizar_libro,crear_autor,crear_libro,AutoresDelete,LibroDelete,eliminarLibro,AutoresViews,AuthService

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', AuthService.as_view(), name='auth'),
    path('autores/', AutoresViews.as_view(), name='autores-list'),
    path('libro/', LibrosViews.as_view(), name='libro-list'),

    # path('selection/<int:pk>/detail/',views.SelectionDetailView.as_view(), name='selection-detail'),
    
    # path('player/<int:pk>/detail/',views.PlayerDetailView.as_view(), name='player-detail'),

    # # Update
    path('autores/<int:pk>/update/', AutoresUpdate.as_view(),name='autores-update'), 
    path('libro/<int:pk>/update/', LibroUpdate.as_view(),name='libro-update'), 
    path('libro/update/<int:pk>/', actualizar_libro,name='libro-update-accion'), 

    
    # #Create
    path('autores/create/',crear_autor, name='autores-create'),
    # path('libro/create/',LibroCreate.as_view(), name='libro-create'),
    path('libro/create/',crear_libro, name='libro-create'),


    # #Delete
    path('autores/<int:pk>/delete/', AutoresDelete.as_view(), name='autores-delete'),
    path('autores/delete/<int:pk>/', AutoresDelete.as_view(), name='autores-delete-accion'),

    path('libro/<int:pk>/delete/',LibroDelete.as_view(), name='libro-delete'),
    path('libro/delete/<int:libro_id>',eliminarLibro, name='libro-delete-accion'),

    path('obtener_autores/', obtener_autores, name='obtener_autores'),
    path('obtener_generos/', obtener_generos, name='obtener_generos'),
    path('obtener_pais/', obtener_paises, name='obtener_pais'),

]
