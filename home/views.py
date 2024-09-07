from django.shortcuts import render, redirect, HttpResponseRedirect
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
    roupa = Estoque.objects.all()
    return render(request, 'home/crud.html', {'form':fm, 'roup':roupa})

# This Function will Update/Edit

def update_data(request, id):
    if request.method == 'POST':
        pi = Estoque.objects.get(pk=id)
        fm = EstoqueRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('crud')
    else:
        pi = Estoque.objects.get(pk=id)
        fm = EstoqueRegistration(instance=pi)
    return render(request, 'home/update.html', {'form': fm})

    # This Function will Delet

def delete_data(request, id):
    if request.method == 'POST':
        pi = Estoque.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')