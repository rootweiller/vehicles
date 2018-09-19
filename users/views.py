from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from users.models import User, Vehicles
from users.serializers import UserSerializers, VehiclesSerializers


class UserCreateView(ListCreateAPIView):

    serializer_class = UserSerializers

    def get_queryset(self):
        """

        :return: <QuerySet [<Vehicles: Chevrolet>, <Vehicles: Toyota>]>
        """
        queryset = User.objects.all()
        return queryset


class VehiclesCreateView(ListCreateAPIView):

    serializer_class = VehiclesSerializers

    def get_queryset(self):
        """

        :return: <QuerySet [<Vehicles: Chevrolet>, <Vehicles: Toyota>]>
        """
        queryset = Vehicles.objects.all()
        return queryset


class VehiclesView(viewsets.ModelViewSet):

    serializer_class = VehiclesSerializers
    model = Vehicles
    queryset = model.objects.all()

    def filter_queryset(self, queryset):
        """

        :param queryset: <QuerySet [<Vehicles: Chevrolet>, <Vehicles: Toyota>]>
        :return: search in queryset
        """
        query = {}
        if self.request.GET.get('license_plate'):
            query['license_plate'] = self.request.GET.get('license_plate')
        if self.request.GET.get('name'):
            query['user__first_name'] = self.request.GET.get('name')
        if self.request.GET.get('dni'):
            query['user__dni'] = self.request.GET.get('dni')
        return self.model.objects.filter(**query)