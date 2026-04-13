import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt
import requests as rq

url = "http://hasanadiguzel.com.tr/api/kurgetir"


response = rq.get(url)
data=response.json()
kurlar = data["TCMB_AnlikKurBilgileri"]
print(kurlar)

df=pd.DataFrame()
dp=pd.DataFrame()
listekorfez=[]
listeasya=[]
for kur in kurlar:
    if kur["Isim"]=="GÜNEY KORE WONU": listekorfez.append(kur)
    elif kur["Isim"]=="ÇİN YUANI": listekorfez.append(kur)
    elif kur["Isim"]=="JAPON YENİ": listekorfez.append(kur)
    elif kur["Isim"]=="İSVEÇ KRONU":  listeasya.append(kur)
    elif kur["Isim"]=="İSVİÇRE FRANGI":  listeasya.append(kur)
    elif kur["Isim"]=="EURO":  listeasya.append(kur) 
    elif kur["Isim"]=="NORVEÇ KRONU":  listeasya.append(kur)

df = pd.DataFrame(listekorfez)
dp = pd.DataFrame(listeasya)

plt.subplot(2,2,1)
ilgilikolonlar=df[["ForexBuying"]].astype(float)

plt.boxplot(ilgilikolonlar)
plt.title("Asya Pasifik Ulkeleri Para Birimi TL Cinsinden Fiyatlari")


plt.subplot(2,2,2)
ilgilikolonlar=dp[["ForexBuying"]].astype(float)
plt.boxplot(ilgilikolonlar)
plt.title("Avrupa Ulkeleri Para Birimi TL Cinsinden Fiyatlari")

plt.show()