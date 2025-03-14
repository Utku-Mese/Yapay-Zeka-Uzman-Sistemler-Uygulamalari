def carpim_tablosu():
    sayi = int(input("Bir sayı giriniz: "))
    for i in range(1, 11):
        print(sayi * i, end=" ")
    print()

def basamak_sayisi():
    sayi = int(input("Bir sayı giriniz: "))
    basamak = 0
    while sayi > 0:
        sayi //= 10
        basamak += 1
    print("Basamak sayısı:", basamak)

def bes_bolunenler():
    sayisalDegerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    for sayi in sayisalDegerler:
        if sayi > 150:
            break
        if sayi % 5 == 0:
            print(sayi, end=", ")
    print()

def aralikta_bolunebilir():
    a = int(input("a değerini giriniz: "))
    b = int(input("b değerini giriniz: "))
    c = int(input("c değerini giriniz: "))
    sayac = sum(1 for i in range(a, b + 1) if i % c == 0)
    print("Bölünebilen sayı adedi:", sayac)

def cift_sayi_ciktisi():
    for i in range(1, 100):
        print(f"{i} - {100 - i}")

def ip_adresi_arttir():
    ip = list(map(int, input("IP adresini giriniz (boşluk ile ayırarak): ").split()))
    for _ in range(5):
        ip[3] += 1
        for i in range(3, -1, -1):
            if ip[i] > 255:
                ip[i] = 0
                if i > 0:
                    ip[i-1] += 1
        print(" ".join(map(str, ip)))

secenekler = {
    "1": carpim_tablosu,
    "2": basamak_sayisi,
    "3": bes_bolunenler,
    "4": aralikta_bolunebilir,
    "5": cift_sayi_ciktisi,
    "6": ip_adresi_arttir
}

secim = input("Çalıştırmak istediğiniz ödevin numarasını giriniz (1-6): ")
if secim in secenekler:
    secenekler[secim]()
else:
    print("Geçersiz seçim!")