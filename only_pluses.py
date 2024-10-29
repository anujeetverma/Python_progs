a = input()
print()
a = int(a)
list= [[],[]]
print(a)
print (list)
for x in range(0,a):
    for y in range (0,3):
        temp =input(y)
        temp = int(temp)
        list[[x][y]] = temp
print(list)