import pandas as pd
from datetime import datetime,timedelta
import streamlit as st


def hesapla(sehir):
    df = pd.read_html(f"https://www.hurriyet.com.tr/{sehir}-namaz-vakitleri/")[0]
    bugun_tarih = datetime.now().date()
    bugun = datetime.now().date().strftime('%d.%m.%Y')
    bugunun_ezanlari = df[df["Tarih"] == bugun].iloc[:, 1:]
    kalan_dakika = None

    for idx, row in bugunun_ezanlari.iterrows():
        for ezan, saat in row.items():
            ezan_saat = datetime.strptime(saat, '%H:%M').time()
            if ezan_saat > datetime.now().time():
                en_yakin_vakit = ezan
                ezan_saati = datetime.combine(datetime.now().date(), ezan_saat)
                sistem_saati = datetime.now()
                fark = ezan_saati - sistem_saati
                kalan_saat = fark.seconds // 3600
                kalan_dakika = (fark.seconds % 3600) // 60
                break

    if kalan_dakika is not None:
        return f"{en_yakin_vakit} vakti için kalan süre: {kalan_saat} saat {kalan_dakika} dakika"

    else:
        yarin_tarih = bugun_tarih + timedelta(days=1)
        yarin = yarin_tarih.strftime('%d.%m.%Y')
        yarinin_ezanlari = df[df["Tarih"] == yarin].iloc[:, 1:]
        imsak_saati = yarinin_ezanlari["İmsak"].values[0]
        imsak = datetime.strptime(imsak_saati, '%H:%M').time()
        ezan_saati = datetime.combine(yarin_tarih, imsak)
        sistem_saati = datetime.now()
        fark = ezan_saati - sistem_saati
        kalan_saat = fark.seconds // 3600
        kalan_dakika = (fark.seconds % 3600) // 60

        if kalan_dakika is not None:
            return f"İmsak vakti için kalan süre: {kalan_saat} saat {kalan_dakika} dakika"

def bugunun_vakitler(sehir):
    df = pd.read_html(f"https://www.hurriyet.com.tr/{sehir}-namaz-vakitleri/")[0]
    bugun_tarih = datetime.now().date()
    bugun = datetime.now().date().strftime('%d.%m.%Y')
    bugunun_ezanlari = df[df["Tarih"] == bugun].iloc[:, 1:]
    return bugunun_ezanlari

def tum_vakitler(sehir):
    df = pd.read_html(f"https://www.hurriyet.com.tr/{sehir}-namaz-vakitleri/")[0]
    return df


st.header("Hoşgeldiniz!")
sehirler=["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]

sehir = st.sidebar.selectbox("Şehir Seç", sehirler)

sehir = sehir.lower()
sehir = sehir.replace("ı","i").replace("ç","c").replace("ö","o").replace("ğ","g").replace("ş","s").replace("ü","u")


st.subheader("Sonraki Vakte Kalan Süre")
st.write(hesapla(sehir))

st.subheader("Bugünün Ezan Vakitleri")
st.markdown(bugunun_vakitler(sehir).style.hide(axis="index").to_html(), unsafe_allow_html=True)

st.subheader("Ezan Vakitleri")
st.markdown(tum_vakitler(sehir).style.hide(axis="index").to_html(), unsafe_allow_html=True)

page = """
<style>
[data-testid="stAppViewBlockContainer"]{
background-image: url(https://e1.pxfuel.com/desktop-wallpaper/121/752/desktop-wallpaper-turkey-mosque-islamic-islamic-android.jpg);
background-size: cover;
}
"""
st.markdown(page,unsafe_allow_html=True)

def add_logo():
    st.markdown(
        """
        <style>
        
            [data-testid="stSidebarContent"]::before {
            content: "Ezan Vakti";
            margin-left: 20px;
            margin-top: 50px;
            margin-bottom: 200px; 
            font-size: 40px;
            position: relative;
            top: 100px;
            }
        
            [data-testid="stSidebarContent"] {
                background-image: url(https://e1.pxfuel.com/desktop-wallpaper/871/576/desktop-wallpaper-islamic-iphone-islam.jpg);
                padding-top: 120px;
                background-size: cover;
            }
            [data-testid="stSidebarContent"]::after {
                content: "https://github.com/mehmetbl";
                margin-left: 20px;
                margin-top: 50px;
                margin-bottom: 200px; 
                font-size: 18px;
                position: relative;
                top: 100px;
            }
            
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()