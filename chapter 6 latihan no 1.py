print ('Menentukan triple pythagoras')
a = int(input ('Masukkan nilai A = '))
b = int(input ('Masukkan nilai B = '))
c = int(input ('Masukkan nilai C = '))

def isPythagoras (a, b, c):
    if (a % 3 == 0 and b % 4 == 0 and c % 5 == 0):
        print ('True, nilai tersebut adalah triple pythagoras')
    elif (a % 5 == 0 and b % 12 == 0 and c % 13 == 0):
        print ('True, nilai tersebut adalah triple pythagoras')
    elif (a % 7 == 0 and b % 24 == 0 and c % 25 == 0):
        print ('True, nilai tersebut adalah triple pythagoras')
    elif (a % 8 == 0 and b % 6 == 0 and c % 10 == 0):
        print ('True, nilai tersebut adalah triple pythagoras')
    elif (a % 9 == 0 and b % 40 == 0 and c % 41 == 0):
        print ('True, nilai tersebut adalah triple pythagoras')
    else :
        print ('False, nilai tersebut adalah bukan triple pythagoras')
isPythagoras (a,b,c)
