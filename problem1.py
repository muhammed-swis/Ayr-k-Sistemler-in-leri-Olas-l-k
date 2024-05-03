import math

def kombinasyon(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def permütasyon(n, k):
    return math.factorial(n) // math.factorial(n - k)

# Çalışan sayıları
toplam_calisan = 15
muhendisler = 6
diger_calisanlar = toplam_calisan - muhendisler - 1  # CEO hariç diğer çalışanlar

# CEO dahil, en az 2 mühendis olacak şekilde 5 kişilik masada oturma düzeni
min_muhendis = 2
max_muhendis = min(5 - 1, muhendisler)  # 5 kişiden biri CEO olduğu için ve en fazla mevcut mühendis kadar

toplam_duzen = 0
for i in range(min_muhendis, max_muhendis + 1):
    yollar_muhendis = kombinasyon(muhendisler, i)
    yollar_diger = kombinasyon(diger_calisanlar, 4 - i)  # 5 kişi içinde 1'i CEO olduğu için
    toplam_duzen += yollar_muhendis * yollar_diger * permütasyon(5, 5)

print(f"Toplantı masasında en az 2 mühendis ve CEO ile birlikte {toplam_duzen} farklı oturma düzeni oluşturulabilir.")
