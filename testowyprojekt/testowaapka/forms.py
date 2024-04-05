from django import forms
from django.core.exceptions import ValidationError
from .models import Uczen, Klasa

class UczenModelForm(forms.ModelForm):
    def clean_form(self):
        imie = self.cleaned_data['imie']
        nazwisko = self.cleaned_data['nazwisko']
        klasa = self.cleaned_data['klasa']
        if isinstance(klasa, str):
            raise ValidationError("Klasa musi byc liczbą")
        return [imie, nazwisko, klasa]
        
    class Meta:
        model = Uczen
        fields = ['imie','nazwisko', 'klasa']

class KlasaModelForm(forms.ModelForm):
    def clean_form(self):
        nazwa = self.cleaned_data['nazwa']
        return nazwa
    
    class Meta:
        model = Klasa
        fields = ['nazwa']