from django.urls import path


from . import views

urlpatterns = [
    path('obat/', views.obat_list, name='obat_list'),
    path('perawatan/', views.perawatan_list, name='perawatan_list'),
    path('penginapan/', views.penginapan_list, name='penginapan_list'),
    path('info/', views.info_list, name='info_list'),
]