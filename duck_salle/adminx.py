import datetime
from django.core.exceptions import ValidationError
from django.forms import Media
from django.views.decorators.cache import never_cache
from django.views.generic import FormView
from duck_salle.models import Reservation
from duck_utils.models import Salle

from xadmin import views
import xadmin
from xadmin.views import filter_hook


class SalleDashboard(views.Dashboard):
    base_template = 'duck_salle/salle_dashboard.html'
    widget_customiz = False

    @never_cache
    def get(self, request, *args, **kwargs):
        self.widgets = self.get_widgets()
        return self.template_response(self.base_template, self.get_context())
xadmin.site.register_view(r'^duck_salle_main/$', SalleDashboard, 'salle_dashboard')


class ConsultationDashboard(views.Dashboard):
#class ConsultationDashboard(FormView):
    base_template = 'duck_salle/consultation_dashboard.html'
    widget_customiz = False

    @never_cache
    def get(self, request, *args, **kwargs):
        self.widgets = self.get_widgets()
        context = self.get_context()
        context['events'] = Reservation.objects.all()
        return self.template_response(self.base_template, context)

    @filter_hook
    def get_media(self, *args, **kwargs):
        return super(ConsultationDashboard, self).get_media(*args, **kwargs) +\
            self.vendor('xadmin.page.form.js', 'xadmin.form.css',
                        'datepicker.js', 'timepicker.js', 'timepicker.css',
                        'xadmin.widget.datetime.js', 'datepicker.css'
                       )

xadmin.site.register_view(r'^duck_salle/consultation/$', ConsultationDashboard, 'consultation_dashboard')

# from django import forms
#
# class SplitTimeWidget(forms.MultiWidget):
#     def __init__(self):
#         widgets = (forms.Select(), forms.Select)
#         super(SplitTimeWidget, self).__init__(widgets)
#
#     def decompress(self, value):
#         print "DECOMPRESS", value
#
# class ReservationForm(forms.ModelForm):
#     # salle = forms.ModelChoiceField(queryset=Salle.objects.all())
#     # label = forms.CharField(max_length=128, required=False)
#     #date = forms.DateField()
#     start_hour = forms.ChoiceField(choices=((i,i) for i in range(24)))
#     start_min = forms.ChoiceField(choices=((i,i) for i in range(60)))
#     end_hour = forms.ChoiceField(choices=((i,i) for i in range(24)))
#     end_min = forms.ChoiceField(choices=((i,i) for i in range(60)), initial=3)
#     # blop = forms.TimeField()
#     blop = forms.CharField(max_length=50, initial='toto')
#     class Meta:
#         model = Reservation
#         fields = ('salle', 'date', 'label')
#
#     # def __init__(self):
#     #     super(ReservationForm, self).__init__()
#     #     print "COUCOU"
#
#     def save(self, commit=True):
#         obj = super(ReservationForm, self).save(commit=False)
#         obj.start = datetime.time(hour=int(self.cleaned_data['start_hour']),
#                                   minute=int(self.cleaned_data['start_min']))
#         obj.end = datetime.time(hour=int(self.cleaned_data['end_hour']),
#                                 minute=int(self.cleaned_data['end_min']))
#         obj.save(commit)
#         return obj


class ReservationAdmin(object):
    pass#form = ReservationForm

xadmin.site.register(Reservation, ReservationAdmin)