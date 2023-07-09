from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import IhaViewset, KiralamaViewset, ProfilViewset, ProfilFotoUpdateView

router = DefaultRouter()
router.register(r'profil', ProfilViewset,  basename="base_profil")
router.register(r'iha', IhaViewset, basename='base_iha')
router.register(r'kiralama', KiralamaViewset, basename='base_kiralama')

urlpatterns = [
    path('', include(router.urls)),
    path('profil_foto/', ProfilFotoUpdateView.as_view(), name='profil-foto'),
]