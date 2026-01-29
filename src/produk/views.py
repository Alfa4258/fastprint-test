from django.shortcuts import render
from .models import Produk
from .forms import ProdukForm
from django.shortcuts import redirect

def home_view(request):
    data_produk = Produk.objects.all()
    return render(request, 'index.html', {'data': data_produk})

def addProduk_view(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdukForm()
    return render(request, 'add_produk.html', {'form': form})

def editProduk_view(request, id):   
    produk = Produk.objects.get(id=id)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'edit_produk.html', {'form': form})

def deleteProduk_view(request, id):
    produk = Produk.objects.get(id=id)
    produk.delete()
    return redirect('home')



