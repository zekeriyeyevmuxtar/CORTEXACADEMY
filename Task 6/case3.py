#Case3 Imtahan ortalamsaına uyğun olaraq Əlaçı, Zərbəçi və ya adi stipeniya alacağını göstərən proqram

print("Imtahan balinizi daxil edin (0-100 arasi):")
imtahan_bali = int(input())

if imtahan_bali > 100 or imtahan_bali < 0:
    print("Daxil etdiyiniz bal yanlisdir. 0-100 arasi bir qiymet daxil edin.")
elif imtahan_bali > 90:
    print("Tebrikler! Siz Əlaçisiniz və stependiya alacaqsınız.")
elif 71 <= imtahan_bali <= 90:
    print("Təbrilər! Siz Zərbəçisiniz və stependiya alacaqsınız.")
elif 51 <= imtahan_bali <= 70:
    print("Təbriklər!  Siz İmtahandan  keçdiz və adi stipeniyası alacaqsınız. Daha yüksək nəticələr üçün üzərinizdə çalışın")
else:
    print("Təsüff ki, kəsildiniz. Həvəsdən düşməyərək daha çox çalışın. Siz bunu bacaracaqsız")

print("Imtahan nəticənizdən razısız? (Hə/Yox)") 
cavab=input()

if cavab== "Hə":
    print("Cavabınızdan qane olduğunuz üçün sevindik. Sükanı belə saxla!")
else:
    print("Cavabınızdan qane deyilsizsə, apleasiya kommusiyyasına müraciət edə bilərsiniz.")    

