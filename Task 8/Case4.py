'''def funk1(*args):
    toplam = sum(*args)
    return toplam

def funk2(cavab):
    for i in range (cavab +1):
        if i%2 ==0:
            print(i)   

ededler = [10,20,30,40,50]
cavab_funk1=ededlerin_cemi(ededler)

cut_ededlerin_capi(cavab_funk1)'''

'''def topla_ededler(arr):
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
cut_ededleri_cap_et(cavab_birinci_funksiyadan)'''











def first(*args):
    cem = 0
    for i in args:
        cem += i
    return cem

print(first(0,1,5,7,12,23,35,40,))

def second():
    massiv = list()
    for i in range(0,124):
        if (i % 2 == 0):
            massiv.append(i)
    return massiv

print(second())