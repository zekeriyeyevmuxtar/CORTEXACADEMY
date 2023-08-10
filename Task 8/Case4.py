

def topla_ededler(arr):
    # List-in içərisindəki bütün ədədləri toplayan funksiya
    toplam = sum(arr)
    return toplam

def cut_ededleri_cap_et(cavab):
    # Birinci funksiyanın cavabını argument kimi alan, 0-dan cavaba qədər olan cüt ədədləri çap edən funksiya
    for i in range(cavab + 1):
        if i % 2 == 0:
            print(i)

# Birinci funksiyayı çağıraraq list-dəki bütün ədədləri toplayırıq
ededler = [10, 20, 30, 40, 50]
cavab_birinci_funksiyadan = topla_ededler(ededler)

# İkinci funksiyanı çağıraraq birinci funksiyanın cavabını argument kimi veririk
cut_ededleri_cap_et(cavab_birinci_funksiyadan)









