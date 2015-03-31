import floppyforms as forms
#from django import forms
from duck_salle.models import Reservation
from xadmin import widgets
from duck_utils.models import Salle


class DatePicker(forms.DateInput):
    template_name = 'duck_salle/widgets/datepicker.html'

class TimePicker(forms.TimeInput):
    template_name = 'duck_salle/widgets/timepicker.html'


class ReservationForm(forms.Form):
    salle = forms.ModelChoiceField(queryset=Salle.objects.all())
    label = forms.CharField(max_length=128, required=False)
    date = forms.DateField(widget=DatePicker)
    start = forms.TimeField()
    end = forms.TimeField()

    def save(self):
        print self.cleaned_data
        r = Reservation(salle=self.cleaned_data['salle'],
                        label=self.cleaned_data['label'],
                        date=self.cleaned_data['date'],
                        start=self.cleaned_data['start'],
                        end=self.cleaned_data['end'])
        r.save()
