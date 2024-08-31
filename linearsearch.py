key = [2,4,6,8,10]
ans = int(input('Enter a number: '))

fun = False

for i in range(0, len(key)):
    if ans == key[i]:
        print('This key exists.')
        fun = True
        break

if fun == False:
    print('This key does not exist.')
