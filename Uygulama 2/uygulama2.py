sayi = float(input("Bir sayı giriniz: "))

if sayi > 0:
    print("Girilen sayı pozitiftir.")

if sayi % 2 == 0:
    print("Girilen sayı çifttir.")
else:
    print("Girilen sayı tektir.")

if sayi < 0:
    print("Girilen sayı negatiftir.")
elif sayi == 0:
    print("Girilen sayı sıfırdır.")
else:
    print("Girilen sayı pozitiftir.")

ağırlık = float(input("Bagajınızın ağırlığını giriniz: "))

if ağırlık > 50:
    print("Bu ağırlıktaki bir çanta için ek ücret ödemeniz gerekmektedir.")
else:
    print("Bagajınızın ağırlığı uygundur.")