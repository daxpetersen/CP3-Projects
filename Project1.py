play = int(input("how many numbers? "))
list = []
secondlist = []
for i in range(play):
    number = int(input("enter a number: "))
    list.append(number)
    print(list)
y=0
x=0
for i in range(play):
    for j in range(play):
        for h in range(play):
            if list[x] >= list[h]:
                x = h
                
            elif list[h] > list[x]:
                continue
    secondlist.append(list[x])
    list.pop(x)
    print(x)        
    print(list)
    print(secondlist)