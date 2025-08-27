Haber Sitesi Django Projesi

Bu proje, Django kullanılarak geliştirilmiş bir haber sitesi uygulamasıdır. Kullanıcıların RSS kaynaklarından haberleri çekmesini, favori haberleri kaydetmesini ve sitede arama yapabilmesini sağlayan interaktif bir web platformudur.

Teknolojiler

Backend: Django 5.0.1

Frontend: HTML, CSS (Bootstrap veya Tailwind CSS kullanılabilir)

Veritabanı: SQLite (geliştirme ortamı için)

RSS Okuma: Python feedparser kütüphanesi

Kullanıcı Yönetimi: Django Auth (kayıt, giriş, çıkış)

Özellikler

RSS Entegrasyonu:

Kullanıcıya haber kaynaklarını takip etme imkânı sunar.

RSS akışlarından otomatik olarak haberleri çeker ve veritabanına kaydeder.

Kullanıcı Kayıt ve Giriş:

Django’nun built-in authentication sistemi kullanılarak güvenli kullanıcı yönetimi.

Giriş yapan kullanıcılar, favori haberlerini görebilir ve yönetebilir.

Favori Haberler:

Her kullanıcı kendi favori haber listesine sahip olur.

Haberler listesinde “Favoriden Kaldır” butonu ile hızlıca yönetilebilir.

Arama Özelliği:

Haber başlığı ve kaynak adı üzerinden dinamik arama yapılabilir.

Kullanıcı dostu ve hızlı bir şekilde arama sonuçları listelenir.

Responsive Tasarım:

Mobil ve masaüstü cihazlarda kullanıcı dostu arayüz.

Kart tabanlı haber listeleme sistemi ile içerik düzeni korunur.

Kurulum ve Kullanım

Projeyi klonlayın:

git clone https://github.com/kullaniciadi/projeadi.git
cd projeadi


Sanal ortam oluşturun ve aktif edin:

python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate


Gereksinimleri yükleyin:

pip install -r requirements.txt


Veritabanını migrate edin:

python manage.py migrate


Sunucuyu başlatın:

python manage.py runserver


Tarayıcıdan http://127.0.0.1:8000/ adresine gidin.

Proje Yapısı
haberler/
├── AppHaberler/           # Ana uygulama
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   └── views.py           # Tüm view fonksiyonları burada
├── haberler/              # Proje ayarları
├── manage.py
├── requirements.txt
└── README.md

Kullanılan Kütüphaneler

Django==5.0.1

feedparser – RSS kaynaklarını okumak için

python-dotenv (isteğe bağlı) – Ortam değişkenlerini yönetmek için

Katkıda Bulunanlar

Meryem Yoncalık – Proje geliştirme, tasarım ve tüm backend/frontend implementasyonu.
