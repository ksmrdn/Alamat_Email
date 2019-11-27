'''
Buatlah sebuah file python interaktif (.py) berisi sebuah function yang dapat menentukan suatu input dari user tergolong alamat email yang valid atau tidak. Adapun kriteria alamat email yang valid adalah sebagai berikut:

Memiliki format: namaUser@namaHosting.ekstensi
namaUser hanya boleh terdiri atas huruf, angka, dash ('-') dan underscore ('_').
namaHosting hanya boleh terdiri atas huruf dan angka.
ekstensi hanya boleh terdiri atas huruf, dengan maksimum 5 karakter.
Contoh:

✅ Alamat email valid:

lintangwisesa@ymail.com
lintang@purwadhika.com
lintang123@ironman123.space

❌ Alamat email tidak valid:
l/nt*ngw:s=s!@ym~il.com
lintang@purwadhika.community
lintang123@ironman123
'''

email = input('Masukkan alamat email: ')

# def cekMail(email):


# print(type(y))
# print(type(y0))
# print(type(y1))


def cekSyb(username):
    state1 = True
    count = 0
    syb = ['/','*',':','=','!','~','#','$','%','^','&','+','(',')','{','}','|','?','<','>']
    while state1 == True:
        for i in syb:
            if i in username:
                print('1. Salah')
                # print('EMAIL TIDAK VALID')
                state1 = False
                return 0
            else:
                count += 1
                if count == 19:
                    print('1. Benar')
                    return 1


def cekHost(hosting):
    state2 = True
    if hosting.isalpha() == True:
        print('2. Benar')
        return 1
    elif hosting.isnumeric() == True:
        print('2. Benar')
        return 1
    elif hosting.isalnum() == True:
        print('2. Benar')
        return 1
    else:
        print('2. Salah')
        state2 = False
        return 0

def cekEx(exten):
    state3 = True
    if 0 < len(exten) < 6:
        if exten.isalpha():
            print('3. Benar')
            return 1
        else:
            print('3. Salah')
            state3 = False
            return 0
    else:
        print('3. Salah')
        state3 = False
        return 0

x = email.split('@')  
if '.' in x[1]:
    x0 = x[0]
    x1 = x[1]
    y = x1.split('.')
    y0 = y[0]
    y1 = y[1]
    cekSyb(x0)
    cekHost(y0)
    cekEx(y1)

    boolList = []
    boolList.append(cekSyb(x0))
    boolList.append(cekHost(y0))
    boolList.append(cekEx(y1))
    print(boolList)
    if 0 in boolList:
        print('HASIL: EMAIL TIDAK VALID')
    else:
        print('HASIL: EMAIL VALID')
else:
    print('HASIL: EMAIL TIDAK VALID')