from django.test import TestCase
from django.utils import timezone

from users.models import Vehicles, User


class VehiclesModelTest(TestCase):

    def create_vehicles(self, brand="Chevrolet", license_plate="ABC-123",
                        type_vehicle="rustic", date_created=timezone.now()):

        user = User.objects.create(password="123456", email="j@dc.com")
        user.save()

        return Vehicles.objects.create(brand=brand, license_plate=license_plate,
                                       type_vehicle=type_vehicle, user=user,
                                       date_created=date_created)

    def test_creation_vehicles(self):

        q = self.create_vehicles()
        self.assertTrue(isinstance(q, Vehicles))
        self.assertEqual(q.__str__(), q.brand)
