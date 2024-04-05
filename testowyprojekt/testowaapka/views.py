from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Klasa, Uczen
from .forms import UczenModelForm, KlasaModelForm
# Create your views here.
def Klasy(request):
    klasy = Klasa.objects.all()
    context = {'klasy':klasy,}
    return render(request, "testowaapka/klasy.html", context=context)

def Uczniowie(request):
    uczniowie = Uczen.objects.all()
    context = {'uczniowie':uczniowie,}
    return render(request, "testowaapka/uczniowie.html", context=context)

def FormularzDodawaniaUcznia(request):
    if request.method == 'POST':
        form = UczenModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("uczniowie")
    else:
        form = UczenModelForm()
    context ={
        'form': form,
    }

    return render(request, "testowaapka/FormularzDodawaniaUcznia.html", context)

def FormularzEdytowaniaUcznia(request,id):
    form = Uczen.objects.get(id=id)
    if request.method == 'POST':
        form.imie = request.POST.get("imie")
        form.nazwisko = request.POST.get("nazwisko")
        form.klasa = Klasa.objects.get(id=request.POST.get("klasa"))
        form.save()
        return redirect("uczniowie")
    return render(request, "testowaapka/edycjauczniow.html", context={'form': form})

def FormularzDodawaniaKlas(request):
    if request.method == 'POST':
        form = KlasaModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("klasy")
    else:
        form = KlasaModelForm()
    context = {
        'form': form
    }
    return render(request, "testowaapka/FormularzDodawaniaKlas.html", context)

def UsuwanieKlas(request):
    form = Klasa.objects.all()
    if request.method == 'POST':
        form = Klasa.objects.get(id = request.POST.get("klasa"))
        form.delete()
        return redirect("klasy")
    return render(request, "testowaapka/usuwanieklas.html")


class UczniowieList(ListView):
    model = Uczen

    def get_queryset(self, *args, **kwargs):
        qs = super(UczniowieList, self).get_queryset(*args,**kwargs)
        # qs = qs.order_by('-id')
        return qs

class UczniowieDetale(DetailView):
    model = Uczen



