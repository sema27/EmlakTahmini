import streamlit as st
import pandas as pd
import joblib

st.title("Emlak Fiyat Tahmini Uygulaması")
binanin_yaslari = pd.read_excel("C:\\Users\\sakar\\ML_Projesi\\VeriToplama\\bina_yasi.xlsx")
isitma_tipleri = pd.read_excel("C:\\Users\\sakar\\ML_Projesi\\VeriToplama\\isitma_tipi.xlsx")

knn_model = joblib.load("C:\\Users\\sakar\\ML_Projesi\\Algoritmalar\\knn_model.pkl")


def binanin_yasi_index(binanin_yasi):
    index = int(binanin_yaslari[binanin_yaslari["Binanin_Yasi"]==binanin_yasi].index.values)
    return index

def isitma_tipi_index(isitma_tipi):
    index = int(isitma_tipleri[isitma_tipleri["Isitma_Tipi"]==isitma_tipi].index.values)
    return index

def esyanin_durumu(esya_durumu):
    if esya_durumu == "Eşyalı":
        return 1
    else:
        return 0

def sitenin_durumu(site_durumu):
    if site_durumu == "Hayır":
        return 1
    else:
        return 0

balkon_sayisi = [0, 1, 2, 3, 4]
binanin_kat_sayisi = [1, 2, 3, 4, 5, 7]
esya_durumu = ["Boş", "Eşyalı"]
banyo_sayisi = [0, 1, 2, 3, 4, 5]
binanin_yasi = ["0-5", "5-10", "11-15", "16-20", "21 Ve Üzeri"]
isitma_tipi = ["Kombi Doğalgaz", "Yerden Isıtma", "Sobalı", "Isıtma Yok", "Doğalgaz Sobalı", "Merkezi Doğalgaz", "Kat Kaloriferi", "Şömine", "Klimalı", "Elektrikli Radyatör", "Merkezi (Pay Ölçer)"]
oda_sayisi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
site_durumu = ["Evet", "Hayır"]


st.sidebar.header("Girdiler")

balkon_sayisi = st.sidebar.selectbox("Balkon Sayısı Seçin", balkon_sayisi)
binanin_kat_sayisi = st.sidebar.selectbox("Bina Kat Sayısı Seçin", binanin_kat_sayisi)
esya_durumu = st.sidebar.selectbox("Esya Durumu Seçin", esya_durumu)
banyo_sayisi = st.sidebar.selectbox("Banyo Sayısını Seçin", banyo_sayisi)
binanin_yasi = st.sidebar.selectbox("Binanın Yaşını Seçin", binanin_yasi)
isitma_tipi = st.sidebar.selectbox("Isıtma Tipini Seçin", isitma_tipi)
net_metrekare = st.sidebar.text_input("Net Metrekare Girin")
oda_sayisi = st.sidebar.selectbox("Oda Sayısı Seçin", oda_sayisi)
site_durumu = st.sidebar.selectbox("Site İçerisinde Olsun Mu?", site_durumu)

def create_prediction_value(Balkon_Sayisi, Binanin_Kat_Sayisi, Esya_Durumu, Banyo_Sayisi, Binanin_Yasi, Isitma_Tipi, Net_Metrekare, Oda_Sayisi, Site_Durumu):
    res = pd.DataFrame(data={'Balkon_Sayisi': [Balkon_Sayisi], 'Binanin_Kat_Sayisi': [Binanin_Kat_Sayisi], 'Esya_Durumu': [Esya_Durumu],
                             'Banyo_Sayisi': [Banyo_Sayisi], 'Binanin_Yasi': [Binanin_Yasi],
                             'Isitma_Tipi': [Isitma_Tipi], 'Net_Metrekare': [Net_Metrekare], 'Oda_Sayisi': [Oda_Sayisi],
                             'Site_Durumu': [Site_Durumu]})
    return res

if st.sidebar.button("Fiyatı Tahmin Et"):
    
    predict_value = create_prediction_value(balkon_sayisi, binanin_kat_sayisi, esyanin_durumu(esya_durumu),
                                           banyo_sayisi, binanin_yasi_index(binanin_yasi),
                                           isitma_tipi_index(isitma_tipi), float(net_metrekare), oda_sayisi,
                                           sitenin_durumu(site_durumu))

    # Tahmin yapma
    knn_prediction = int(knn_model.predict(predict_value).item())

    # Sonucu ekrana yazdırma
    st.header("Tahmin Edilen Fiyat")
    st.write("K-Nearest Model Result:", knn_prediction, "TL")

