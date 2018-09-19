from django.conf.urls import url

from .views import UserCreateView, VehiclesCreateView, VehiclesView

vehicles = VehiclesView.as_view({
    'get':'list'
})

urlpatterns = [
    url(r'^$', UserCreateView.as_view(), name='event_history'),
    url(r'^vehicles/$', VehiclesCreateView.as_view(), name='vehicles'),
    url(r'^vehicles/search/', vehicles, name='vehicles_search'),

]