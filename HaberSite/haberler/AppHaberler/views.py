from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
import feedparser
from datetime import datetime
from bs4 import BeautifulSoup
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Favorite
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Favorite  # Favorileri tuttuğun model

# HTML içindeki metni temizleyen ve haberleri işleyen yardımcı fonksiyon
def parse_haberler(rss_url):
    feed = feedparser.parse(rss_url)
    haberler = []

    for haber in feed.entries:
        haber_dict = {
            "kaynak": "EnSonHaber",
            "baslik": haber.title,
            "link": haber.link
        }

        dt = datetime.strptime(haber.published, '%a, %d %b %Y %H:%M:%S %z')
        haber_dict["date"] = dt.strftime('%d-%m-%Y %H:%M:%S')

        soup = BeautifulSoup(haber.summary, 'html.parser')
        haber_dict["description"] = soup.get_text()

        image_url = None
        if 'media_content' in haber and len(haber.media_content) > 0:
            image_url = haber.media_content[0]['url']
        elif 'enclosures' in haber and len(haber.enclosures) > 0:
            image_url = haber.enclosures[0]['url']

        if image_url:
            haber_dict["image"] = image_url
            haberler.append(haber_dict)
        else:
            print("⚠️ Görsel bulunamadı, haber atlandı:", haber.title)

    return haberler

# Footer için popüler haberler (genelde ana feed'den ilk 4 haber)
def get_footer_haberler():
    return parse_haberler("https://www.ensonhaber.com/rss/ensonhaber.xml")[:4]

# Ana sayfa
def index(request):
    categorys = Category.objects.all()
    haberler = parse_haberler("https://www.ensonhaber.com/rss/ensonhaber.xml")

    context = {
        "haberler": haberler,
        "categorys": categorys,
        "footer_haberler": get_footer_haberler()
    }
    return render(request, "index.html", context)

# Kategori sayfaları
def category(request, category):
    categorys = Category.objects.all()

    rss_urls = {
        "politika": "https://www.ensonhaber.com/rss/politika.xml",
        "ekonomi": "https://www.ensonhaber.com/rss/ekonomi.xml",
        "teknoloji": "https://www.ensonhaber.com/rss/teknoloji.xml",
        "spor": "https://www.ensonhaber.com/rss/kralspor.xml",
        "saglk": "https://www.ensonhaber.com/rss/saglik.xml",
        "dunya":"https://www.ensonhaber.com/rss/dunya.xml",
        "kultur-sanat":"https://www.ensonhaber.com/rss/kultur-sanat.xml",
        "magazin": "https://www.ensonhaber.com/rss/magazin.xml",
        "kadn": "https://www.ensonhaber.com/rss/kadin.xml"
    }

    if category in rss_urls:
        haberler = parse_haberler(rss_urls[category])
    else:
        haberler = []

    context = {
        "haberler": haberler,
        "categorys": categorys,
        "category": category,
        "footer_haberler": get_footer_haberler()
    }
    return render(request, "category.html", context)
def search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        rss_url = "https://www.ensonhaber.com/rss/ensonhaber.xml"
        feed = feedparser.parse(rss_url)

        for haber in feed.entries:
            if query.lower() in haber.title.lower() or query.lower() in haber.summary.lower():
                dt = datetime.strptime(haber.published, '%a, %d %b %Y %H:%M:%S %z')
                soup = BeautifulSoup(haber.summary, 'html.parser')
                image_url = None
                if 'media_content' in haber and len(haber.media_content) > 0:
                    image_url = haber.media_content[0]['url']
                elif 'enclosures' in haber and len(haber.enclosures) > 0:
                    image_url = haber.enclosures[0]['url']

                if image_url:
                    results.append({
                        "kaynak": "EnSonHaber",
                        "baslik": haber.title,
                        "link": haber.link,
                        "date": dt.strftime('%d-%m-%Y %H:%M:%S'),
                        "description": soup.get_text(),
                        "image": image_url
                    })

    categorys = Category.objects.all()

    # 🔥 eksik olan footer haberlerini ekliyoruz:
    footer_haberler = parse_haberler("https://www.ensonhaber.com/rss/ensonhaber.xml")[:4]

    return render(request, "search_results.html", {
        "query": query,
        "results": results,
        "categorys": categorys,
        "footer_haberler": footer_haberler  # 💡 bu satır kritik!
    })

@login_required
def add_favorite(request):
    if request.method == "POST":
        baslik = request.POST.get("baslik")
        link = request.POST.get("link")
        kaynak = request.POST.get("kaynak")
        tarih = request.POST.get("tarih")
        resim = request.POST.get("resim")

        if not Favorite.objects.filter(user=request.user, haber_link=link).exists():
            Favorite.objects.create(
                user=request.user,
                haber_baslik=baslik,
                haber_link=link,
                haber_kaynak=kaynak,
                haber_tarih=tarih,
                haber_resim=resim
            )
    return redirect(request.META.get('HTTP_REFERER', '/'))

from .models import Category  # kategoriler modelin varsa

@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    categorys = Category.objects.all()  # kategorileri alıyoruz
    return render(request, 'favorites.html', {
        'favorites': favorites,
        'categorys': categorys  # template’e gönderiyoruz
    })


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2 and username and email:
            User.objects.create_user(username=username, email=email, password=password1)
            messages.success(request, "Kayıt başarılı! 🎉")
            return redirect("register")  # tekrar aynı sayfaya yönlendir
        else:
            messages.error(request, "Eksik bilgi veya şifreler uyuşmuyor.")

    return render(request, "register.html")

@login_required
def remove_favorite(request, fav_id):
    favorite = get_object_or_404(Favorite, id=fav_id, user=request.user)
    favorite.delete()
    return redirect('favorites_list')
