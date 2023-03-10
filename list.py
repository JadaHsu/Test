list = input()
list = str(list)
odd = []
even = []
for number in range(len(list)):
    c = eval(list[number])
    if c%2 == 0:
        even.append(list[number])
    else:
        odd.append(list[number])

list_odd = sorted(odd,reverse=True)
list_even =sorted(even)

d = ''.join(map(str, list_odd)) + ''.join(map(str, list_even))

print(d)
