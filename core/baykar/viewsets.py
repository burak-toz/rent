from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django.db.models import Q

# Permissions
from .permissions import IsOwnerProfilPermission

from .models import Iha, Kiralama, Profil
from .serialzers import IhaSerializer, KiralamaSerializer, ProfilSerializer, ProfilFotoSerializer


class ProfilViewset(ModelViewSet):
    serializer_class = ProfilSerializer
    permission_classes = [IsOwnerProfilPermission]

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Profil.objects.all()
        else:
            queryset = Profil.objects.filter(user=self.request.user)

        return queryset



class ProfilFotoUpdateView(UpdateAPIView):

    serializer_class = ProfilFotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profil_nesnesi = self.request.user.profil
        return profil_nesnesi


class IhaViewset(ModelViewSet):

	queryset = Iha.objects.all()
	serializer_class = IhaSerializer
	filter_backends = [SearchFilter]
	search_fields = ["marka", "model"]

class KiralamaViewset(ModelViewSet):

	# queryset = Kiralama.objects.all()
	serializer_class = KiralamaSerializer

	def get_queryset(self):
		queryset = Kiralama.objects.all()
		search = self.request.query_params.get('search')

		if search is not None and search != "":
			queryset = queryset.filter(Q(iha__model__contains=search) | Q(uye__username__contains=search))
		return queryset
