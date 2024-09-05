from django.core import validators
from django import forms
from .models import Estoque

class EstoqueRegistration(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['marca', 'produto', 'genero', 'quantidade', 'preco']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'produto': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        
        labels = {
            'marca': 'Nome da Marca',
            'produto': 'Produto',
            'genero': 'Gênero',
            'quantidade': 'Quantidade em Estoque',
            'preco': 'Preço',
        }