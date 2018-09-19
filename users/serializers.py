from rest_framework import serializers

from users.models import User, Vehicles


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class VehiclesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Vehicles
        fields = '__all__'
