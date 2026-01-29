from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Produk
from .forms import ProdukForm

def home_view(request):
    data_produk = Produk.objects.select_related('kategori', 'status').filter(status__nama_status__icontains="bisa dijual")
    return render(request, 'index.html', {'data': data_produk})

def add_produk_view(request):
    form = ProdukForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produk berhasil ditambahkan!')
        return redirect('home')
    return render(request, 'add_produk.html', {'form': form})

def edit_produk_view(request, id):   
    produk = get_object_or_404(Produk, id=id)
    form = ProdukForm(request.POST or None, instance=produk)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produk berhasil diperbarui!')
        return redirect('home')
    return render(request, 'edit_produk.html', {'form': form})

@require_POST
def delete_produk_view(request, id):
    produk = get_object_or_404(Produk, id=id)
    produk.delete()
    messages.success(request, 'Produk berhasil dihapus!')
    return redirect('home')



