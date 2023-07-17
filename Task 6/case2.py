# prava məsələsi

print("Yaşınızı daxil edin:")
yas = int(input())

print("Əlillik probleminiz varmı varmı? (Hə/Yox):")
elillik_problemi = input()  

# Yaş və əlilliyin  yoxlanılması
if yas >= 18 and elillik_problemi == "Yox":
    print("Sürücülük vəsiqəsi əldə edə bilərsiniz. Təbrik edirik.")
else:
    print("Sürücülük vəsiqəsi  almağ üçün şərtləri qarşılamırsınız.")
