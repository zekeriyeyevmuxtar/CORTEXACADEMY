 # Obiyekt yonlu proqramlasdirma (OOP)- funksiyalar, def' | call etmek

'''def funksiyadadi(): #passiv veziyyetdedi
    emeliyyatlar       

funksiyadadi() # aktiv hali  '''


'''def adiniz(): #passiv
    
    print('Muxtar')

adiniz() #aktiv edildi

def topla():
    a=5
    b=2
    print(a+b)

topla()

def toplamaq(a,b):
    print(a+b)
toplamaq(5,2) #arqument teyin etmek    '''

def funk(**dic):
    for key, value in dic.items():
        print('istifadecinin   ' + key +' ' + value + 'dir')
       return print('----------------------------------------')

print(funk(adı = 'Muxtar', soyadi = 'Zekeriyeyev', maili ='zekeriyeyevmuxtar547@gmail.com'))
print(funk(adı = 'Merdan', soyadi = 'Haciyev', maili ='merdan.hacili.2004@gmail.com'))
print(funk(adı = 'Vusal', soyadi= 'Heydarov', maili ='usal_heydarov123@gmail.com'))