# laporan/forms.py

from django import forms
from .models import Laporan

class NameForm(forms.Form):
    your_name = forms.CharField(label='Nama Kamu ', max_length=5)

class LaporanForm(forms.ModelForm):
    class Meta:
        model = Laporan
        fields = '__all__'
        exclude = ['pelapor', 'status']