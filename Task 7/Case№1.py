# Tək ədədləri ekranda yan-yana yazdırmaq üçün
for i in range(1, 101, 2):
    print(i, end=" ")

print()  # Satırı bitirmek üçün boş satır etdim ki yeni sətirə keçsin və tək ədədlərlə cüt ədədlər qarşımasın

# Cüt ədədləri listə əlavə etmək və listi çap etmək
cüt_ədədlər = []
for i in range(2, 101, 2):
    cüt_ədədlər.append(i) #Listdeki  .append() metodu, verilən dəyəri listin sonuna əlavə edir. Dövürdən yaranan hər yeni cüt ədədi listin sonuna əlavə edəcək.

print(cüt_ədədlər)
