#cityname=['Baki','moskova','Tiblis', 'tehran','Ankara', 'Istanbul','tokyo','Vasikton']

city_name = ['Baki', 'moskova', 'Tiblis', 'tehran', 'Ankara', 'Istanbul', 'tokyo', 'Vasikton']

# Yeni bir boş list yaradırıq
new_cityname_list = []

# Şəhər adlarını ən azı bir dəfə oxuyuruq
for city in city_name:
    # if vasitəsi ilə tək tək şəhər adlarıın ilk hərfini yoxlayırıq və əgər bu hərf kiçikdirsə həmin şəhər adını yeni listə əlavə edirik.
    if city[0].islower():
        new_cityname_list.append(city)

# Nəticəni çap edirik
print(city_name)
print(new_cityname_list)



