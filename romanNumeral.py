
r = 'MMCDXXXIV'

dict = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
}

numbers = []

sum = 0

i = 0

while len(r) > i:
    if(dict[r[i]] >= dict[r[i + 1]]):
        sum = sum + dict[r[i]]
        i = i + 1
    else:
        sum = sum + (dict[r[i + 1]] - dict[r[i]])
        i = i + 2
        
print(sum)
