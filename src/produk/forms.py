from .models import Produk
from django import forms

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']
        widgets = {
            'nama_produk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama produk'
            }),
            'harga': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'placeholder': 'Masukkan harga'
            }),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
