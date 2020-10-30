def starFormation1(n):
    i = 0
    while(i < n):
        j = 0
        while(j <= i):
            print('*', end="")
            j+=1
        print(' ')
        i += 1
def starFormation2(n):
        i = 0
        while(i < n):
            j = n
            while(j > i):
                print('*', end="")
                j -= 1
            print(' ')
            i += 1
def starFormation3(n):
    starFormation1((n//2+1))
    starFormation2((n//2))
starFormation3(7)
