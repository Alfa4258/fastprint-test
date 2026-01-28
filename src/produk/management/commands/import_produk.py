from django.core.management.base import BaseCommand
import requests
import hashlib
from datetime import datetime, timedelta

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

        username = f"tesprogrammer{(datetime.now()+ timedelta(hours=7)).strftime('%d%m%yC%H')}"
        print(f"generated username: {username}")

        password = f"bisacoding-{(datetime.now() + timedelta(hours=7)).strftime('%d-%m-%y')}"
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        payload = {
            "username" : username,
            "password" : hashed_password
        }
        response = requests.post(url, data=payload)
        print(f"response status code: {response.status_code}")
        print(f"response body: {response.json()}")
        
        
