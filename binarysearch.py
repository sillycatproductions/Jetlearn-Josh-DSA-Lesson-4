key = [1,2,3,4,5,6,7,8,9,10]
aaa = int(input('Search number: '))

start = 0
end = len(key) - 1
midpoint = (start + end) // 2
found = False

while start <= end:
    midpoint = (start + end) // 2
    if key[midpoint] == aaa:
        print('Key found.')
        found = True
        break
    elif key[midpoint] < aaa:
        start = midpoint + 1
    else:
        end = midpoint - 1
    
if found == False:
    print('Key not found.')
    