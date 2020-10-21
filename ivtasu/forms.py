from django import forms
from .models import Zanyatia
from .models import Days


class ZanyatiaForm(forms.ModelForm):
    class Meta:
        model = Zanyatia
        fields = ('name', 'lector', 'time_start', 'time_end')


class DaysForm(forms.ModelForm):
    class Meta:
        model = Days
        fields = ('day', 'spisok')
