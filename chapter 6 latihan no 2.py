print('ke 1')
def starFormation1 (n):
    i = 0
    while (i < n):
        i += 1
        print ('* ' * i)
starFormation1 (4)
print('')
print('ke 2')
def starFormation2 (n):
    print ('* ' * n) 
    while (n > 0):
        n -= 1
        print ('* ' * n)
starFormation2(4)

print('ke 3')
def starFormation3 (n):
    i = 0
    while ( i < n/2 ):
        i += 1
        print ('* ' * i)
    while ( i >= n/2 or i > 0):
        i -= 1
        print ('* ' * i)
        
starFormation3 (7)

