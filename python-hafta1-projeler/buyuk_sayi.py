#Kullanıcıdan alınan iki sayıdan büyük olanı yazdıran program
#Kullanıcıdan sayıları alıyoruz
sayi1 = int(input("Lütfen ilk sayıyı giriniz :"))
sayi2 = int(input("Lütfen ikinici sayıyı giriniz :"))

if sayi1 < sayi2 :
    print(f"Büyük olan sayı --> {sayi2}")
elif sayi1 == sayi2 :
    print("Sayılar eşittir")
else:
    print(f"Büyük olan sayı --> {sayi1}")