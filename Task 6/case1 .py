#sual №1 17+8 in cavabi
A = 25
B = 24
C = 26
print("17 + 8 cavabi neye beraberdir? (A, B veya C)  \n A) 25 \n B) 24 \n C) 26 ")

cavab = input().upper()  # İstifadəçinin0 girişini böyük həriflə daxil etməsini isteyirəm

if cavab == "A":
    print('Cavab duzgundur')
elif cavab == "B":
    print('Cavab duzgun deyil')
elif cavab == "C":
    print('Cavab duzgun deyil')
else:
    print('Daxil etdiyiniz cavab formati yanlışdır')

#sual №2 17+8 in kvadratı neçə edir?

D = 655
F = 615   
duzgun_cavab= (17+8)**2
E = duzgun_cavab
print("17 + 8 kvadratı  neye beraberdir? (D, E veya F)  \n D) 655 \n E) 625 \n F) 615 ")
cavab2 = input().upper()
if cavab2 == "E":
    print('Cavab duzgundur')
elif cavab2 == "D":
    print('Cavab duzgun deyil')
elif cavab2 == "F":
    print('Cavab duzgun deyil')
else:
    print('Daxil etdiyiniz cavab formati duzgun deyil')
