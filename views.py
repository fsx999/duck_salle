import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from duck_salle.forms import ReservationForm
from duck_salle.models import Reservation
from duck_salle.serializers import SalleSerializer, ReservationSerializer
from duck_utils.models import Salle


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class SalleView(APIView):

    def get(self, request):
        salles = Salle.objects.all()
        serializer = SalleSerializer(salles, many=True)
        return JSONResponse(serializer.data)

#
# class ReservationView(APIView):
#     def get(self, request):
#         reservations = self.get_queryset() #Reservation.objects.all()
#         serializer = ReservationSerializer(reservations, many=True,
#                                            context={'request': request})
#         return JSONResponse(serializer.data)
#
#     def get_queryset(self):
#         # Used to get the interval
#         from_date = self.request.GET.get('from', None)
#         to_date = self.request.GET.get('to', None)
#
#         print from_date, to_date
#         if from_date and to_date:
#             pass # return Reservation.objects.filter()
#         return Reservation.objects.all()

class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class SalleViewSet(ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer

class ReservationEventsView(APIView):
    def get(self, request):
        """
        Return a json event list for use with fullCalendar (js)
        """
        start_date = request.GET.get('start', None)
        end_date = request.GET.get('end', None)
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None
        if not start_date:
            objects = Reservation.objects.all()
        else:
            objects = Reservation.objects.filter(date__gte=start_date,
                                                 date__lte=end_date)
        json_list = []
        for o in objects:
            json_list.append({
                'id': o.id,
                'title': "{}\n{}".format(o.salle.label, o.label),
                'start': "{}T{}".format(o.date, o.start),
                'end': "{}T{}".format(o.date, o.end),
            })
        return JSONResponse(json_list)


class ReservationFormView(FormView):
    form_class = ReservationForm
    template_name = 'duck_salle/reservation_form.html'

    def get_success_url(self):
        return reverse('reservation_form')

    def get_initial(self):

        initial = super(ReservationFormView, self).get_initial()
        if self.request.GET.get('date', None):
            initial['date'] = self.request.GET.get('date', None)
            initial['start'] = self.request.GET.get('start', None)
            initial['end'] = self.request.GET.get('end', None)

        return initial

    def form_valid(self, form):

        form.save()
        return HttpResponse('super tout baigne')
        # return super(ReservationFormView, self).form_valid(form)


# DOES NOT WORK: TemplateDoesNotExist: rest_framework/api.html
# class ReservationView(generics.ListAPIView):
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer
