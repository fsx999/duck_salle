from django.conf.urls import url, include
from rest_framework import routers
from duck_salle import views

router = routers.DefaultRouter()
router.register(r'reservations', views.ReservationView)
router.register(r'salles', views.SalleViewSet)

urlpatterns = [
    # url('^salles/$',
    #     views.SalleView.as_view(),
    #     name='duck_salle_salles'),
    url(r'^', include(router.urls)),
    # url('^reservations/$',
    #     views.ReservationView.as_view(),
    #     name='duck_salle_reservations'),
    url('^reservation_events/$',
        views.ReservationEventsView.as_view(),
        name='duck_salle_reservation_events'),
    url('^reservation_form/$', views.ReservationFormView.as_view(),
        name='reservation_form')

]