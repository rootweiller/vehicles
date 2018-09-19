from django.contrib import admin

from users.models import Vehicles, User


class VehiclesAdmin(admin.ModelAdmin):

    list_display = ('brand', 'license_plate',
                    'type_vehicle')


admin.site.register(Vehicles, VehiclesAdmin)


class UserAdmin(admin.ModelAdmin):

    list_display = ('dni', 'email', 'date_joined')


admin.site.register(User, UserAdmin)
