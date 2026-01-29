# FastPrint - Aplikasi Manajemen Produk

Aplikasi web Django untuk manajemen data produk dengan fitur CRUD dan import data dari file.

## Teknologi

- Python 3.x
- Django 5.2
- MySQL 8.0
- Docker & Docker Compose

## Instalasi

### Menggunakan Docker 

1. Clone repository
```bash
git clone <repository-url>
cd fastprint-test
```

2. Jalankan Docker Compose
```bash
docker-compose up --build
```

3. Akses aplikasi di `http://localhost:8000`

### Tanpa Docker

1. Clone repository dan buat virtual environment
```bash
git clone <repository-url>
cd fastprint-test
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Copy dan konfigurasi environment
```bash
cp .env.example .env
# Edit .env sesuai konfigurasi database lokal
```

4. Jalankan migrasi dan server
```bash
cd src
python manage.py migrate
python manage.py runserver
```

## Struktur Folder

```
fastprint-test/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── src/
    ├── manage.py
    ├── config/          # Konfigurasi Django
    └── produk/          # Aplikasi produk (models, views, templates)
```

## Fitur
- Daftar produk dengan pagination
- Tambah, edit, hapus produk
- Import produk dari file
- Format harga dengan pemisah ribuan
