import math

# Toplam çalışan, mühendis sayısı ve oda sayısı
toplam_calisan = 25
muhendis_sayisi = 10
oda_sayisi = 8

# Güvercin yuvası ilkesine göre genel çalışan hesaplama
en_az_calisan = math.ceil(toplam_calisan / oda_sayisi)

# Her odada en az bir mühendis olması durumu
# En az bir mühendis olan odalar
en_az_bir_muhendis_odalari = min(oda_sayisi, muhendis_sayisi)
# Geri kalan çalışanlar
geri_kalan_calisanlar = toplam_calisan - en_az_bir_muhendis_odalari

# En az iki kişi olması gereken odalar
en_az_iki_kisi = math.ceil(geri_kalan_calisanlar / en_az_bir_muhendis_odalari)

print(f"Herhangi bir odada en az {en_az_calisan} çalışan bulunmalıdır.")
print(f"Her odada en az bir mühendis bulunduğunda, en az {en_az_iki_kisi} odada en az iki kişinin olması gerekmektedir.")
