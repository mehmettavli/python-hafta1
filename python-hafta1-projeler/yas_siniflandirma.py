#Kullanıcan yas alma programı
#Kullanıcının yasını öğreniyoruz
yas = int(input("Lütfen yaşınızı giriniz :"))

if 0 <= yas <= 12  :
    print("Çocuk")
    
elif 13 <= yas <= 17:
    print("Genç")
    
elif 18 <= yas <= 64:
    print("Yetişkin")
    
elif 65 <= yas :
    print("Yaşlı")
    
else:
    ("Lütfen yaşınızı rakamlar ile belirtiniz.")