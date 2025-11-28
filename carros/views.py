from django.shortcuts import render
from .models import Carro
from .forms import CarroForm

def index(request):
    carros = Carro.objects.all()
    
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CarroForm()
    
    context = {
        'carros': carros,
        'form': form,
    }
    return render(request, 'carros/index.html', context)
