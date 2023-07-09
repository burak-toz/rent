from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django.db.models import Q

# Permissions
from .permissions import IsOwnerProfilPermission

# Paginations
from .paginations import SmallOffsetPaginations

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
	pagination_class = SmallOffsetPaginations

	def get_queryset(self):
		queryset = Kiralama.objects.all()
		search = self.request.query_params.get('search[value]')
		iha = self.request.query_params.get('columns[0][search][value]')
		uye = self.request.query_params.get('columns[1][search][value]')



		if search is not None and search != "":
			queryset = queryset.filter(Q(iha__model__contains=search) | Q(uye__username__contains=search))

		if iha is not None and iha != "":
			queryset = queryset.filter(Q(iha__model__icontains=iha) | Q(iha__marka__icontains=iha))

		if uye is not None and uye != "":
			queryset = queryset.filter(uye__username__contains=uye)


		return queryset

	def list(self, request, *args, **kwargs):

		queryset = self.filter_queryset(self.get_queryset())

		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(queryset, many=True)
		return Response({"data": serializer.data})
