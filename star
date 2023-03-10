n = input()
n = int(n)
# n = 5
for i in range(n):
    for a in range(n-i-1):
        print(' ',end='')
    for b in range(2*i+1):  
        if b%2 == 0:
            print('*',end='')
        else:
            print(' ',end='')
    print('\n',end='')  
