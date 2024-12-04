from django.views.generic import ListView

from app.models import *
from django.shortcuts import render





from django.shortcuts import render
from .models import KopSotilganKitob, kun_iqtibos,Kitob

def index(request):
    kop_sotilgan = KopSotilganKitob.objects.all()
    iqtibos = kun_iqtibos.objects.all()
    return render(request, 'index.html', {'kop': kop_sotilgan, 'iqtibos': iqtibos})


from django.shortcuts import render
from .models import KopSotilganKitob

def kitob_malumotlari(request):
    search_query = request.GET.get('search', '')
    if search_query:
        kitoblar = Kitob.objects.filter(nomi__icontains=search_query)
    else:
        kitoblar = Kitob.objects.all()
    return render(request, 'second.html', {'kitob': kitoblar})
