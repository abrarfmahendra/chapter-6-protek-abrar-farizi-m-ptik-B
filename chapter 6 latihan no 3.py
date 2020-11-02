def faktorial(n):
    if (n==1):
        return 1
    elif (n==0):
        return 1
    else :
        return (n * faktorial(n-1))
def kombinasi (a, b):
    hasil = faktorial(a)/(faktorial(a-b) * faktorial(b))
    print ('Kombinasi dari ', a,'C', b, 'yaitu ',hasil)

def permutasi (a, b):
    hasil = faktorial(a)/ faktorial(a-b)
    print ('Kombinasi dari ', a,'P', b,'yaitu ',hasil)
kombinasi(5,3)
permutasi(10,7)
