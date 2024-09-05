from django.shortcuts import render
from .forms import EstoqueRegistration
from .models import Estoque

# Create your views here.

# This Function Will Add new Item and Show All Items

def crud(request):
    if request.method == 'POST':
        fm = EstoqueRegistration(request.POST)
        if fm.is_valid():
            mr = fm.cleaned_data['marca']
            pd = fm.cleaned_data['produto']
            gn = fm.cleaned_data['genero']
            qt = fm.cleaned_data['quantidade']
            pc = fm.cleaned_data['preco']
            reg = Estoque(
                marca=mr, 
                produto=pd, 
                genero=gn,
                quantidade=qt,
                preco=pc
                )
            reg.save()
            fm = EstoqueRegistration()
    else:
        fm = EstoqueRegistration()
    # roupa = Estoque.objects.all()
    return render(request, 'home/crud.html', {'form':fm})