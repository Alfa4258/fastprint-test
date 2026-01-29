from urllib import response
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from produk.models import Kategori, Status, Produk
import requests
import hashlib

class Command(BaseCommand):
    help = 'Import produk dari API eksternal'

    def handle(self, *args, **kwargs):
        print("--- Starting Command ---")
        url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'
        #response = requests.get(url)
        #print(f"Status Code: {response.status_code}")
        #print(f"Raw Data: {response.json()}")
        #data = response.json()
        #for item in data:  
        #    print(item)

        username = f"tesprogrammer{(datetime.now() + timedelta(hours=7)).strftime('%d%m%yC%H')}"
        print(f"generated username: {username}")

        password = f"bisacoding-{(datetime.now() + timedelta(hours=7)).strftime('%d-%m-%y')}"
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        payload = {
            "username" : username,
            "password" : hashed_password}
        
        response = requests.post(url, data=payload)
        print(f"response status code: {response.status_code}")
        print(f"response body: {response.json()}")

        data_produk = response.json()['data']
        for item in data_produk:
            harga_angka = int(item['harga'])
            kategori_obj, created = Kategori.objects.get_or_create(
                nama_kategori=item['kategori'])
            status_obj, created = Status.objects.get_or_create(
                nama_status=item['status'])
            produk_obj, created = Produk.objects.get_or_create(
                nama_produk=item['nama_produk'],
                harga=harga_angka,
                kategori=kategori_obj,
                status=status_obj)
            
            if created:
                self.stdout.write(self.style.SUCCESS(f"Berhasil menambah: {produk_obj.nama_produk}"))
            else:
                self.stdout.write(self.style.WARNING(f"Produk sudah ada: {produk_obj.nama_produk}"))
        