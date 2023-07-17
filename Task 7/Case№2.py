import random

random_number = random.randint(1, 10)
şans = 3

while şans > 0:
    istifadəçinin_təxmini = int(input("1 ilə 10 arasında bir rəqəm təxmin edin: "))

    if istifadəçinin_təxmini == random_number:
        print("Təbriklər! Düzgün cavabı tapdınız.")
        break

    şans -= 1
    if şans > 0:
        print("Bir daha sınayın." + str(şans) + " şansınız qalıb.")
    

if şans == 0 and istifadəçinin_təxmini != random_number:
    print("Təəssüfki, düzgün cavabı tapa bilmədiniz.")
    
    print("Yenidən oynamaq üçün proqramı təkrar işə salın.")
