#project : 9 rooms,
#travel or leave rooms
#map to what rooms connect to what
#player stats
#Final Boss(other enemies)
#items can be picked up 
#items/monsters repopulate
x = "X"
posx = 0
posy = 0
map = ((("A"),("B"),("C"),("D"),("E")),
(("F"),("G"),("H"),("I"),("J")),
(("K"),("L"),("M"),("N"),("O")),
(("P"),("Q"),("R"),("S"),("T")),
(("U"),("V"),("W"),("X"),("Y")))
map1 = ((("A"),("B"),("C"),("D"),("E")),
(("F"),("G"),("H"),("I"),("J")),
(("K"),("L"),("M"),("N"),("O")),
(("P"),("Q"),("R"),("S"),("T")),
(("U"),("V"),("W"),("X"),("Y")))
map2 = ((("A"),("B"),("C"),("D"),("E")),
(("F"),("G"),("H"),("I"),("J")),
(("K"),("L"),("M"),("N"),("O")),
(("P"),("Q"),("R"),("S"),("T")),
(("U"),("V"),("W"),("X"),("Y")))
map3 = ((("A"),("B"),("C"),("D"),("E")),
(("F"),("G"),("H"),("I"),("J")),
(("K"),("L"),("M"),("N"),("O")),
(("P"),("Q"),("R"),("S"),("T")),
(("U"),("V"),("W"),("X"),("Y")))
map4 = ((("A"),("B"),("C"),("D"),("E")),
(("F"),("G"),("H"),("I"),("J")),
(("K"),("L"),("M"),("N"),("O")),
(("P"),("Q"),("R"),("S"),("T")),
(("U"),("V"),("W"),("X"),("Y")))
list = []
play = input("r to start: ")
number = 0
print("W: North, A: West, D: East, S: South")
new = map[posy][posx]

new1 = 0








while play != "e":
        if new == "A":
            print("O","X","U","U","U")
            print("X","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","E","U")
            list.append("A")
            new = map[posy][posx]


        elif new == "B":
            print("X","O","X","U","U")
            print("U","X","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","E","U")
            list.append("B")
            new = map[posy][posx]


        elif new == "C":
            print("U","X","O","X","U")
            print("U","U","X","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","E","U")
            list.append("C")
            new = map[posy][posx]


        elif new == "D":
            print("U","U","X","O","X")
            print("U","U","U","X","U")
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","E","U")
            list.append("D")
            new = map[posy][posx]


        elif new == "E":
            print("U","U","U","X","O")
            print("U","U","U","U","X")
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","E","U")
            list.append("E")
            new = map[posy][posx]





        if new == "F":
            print("X","U","U","U","U")
            print("O","X","U","U","U")
            print("X","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","E","U")
            list.append("F")
            new = map[posy][posx]


        elif new == "G":
            print("U","X","U","U","U")
            print("X","O","X","U","U")
            print("U","X","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","E","U")
            list.append("G")
            new = map[posy][posx]


        elif new == "H":
            print("U","U","X","U","U")
            print("U","X","O","X","U")
            print("U","U","X","U","U")
            print("U","U","U","U","U")
            print("U","U","U","E","U")
            list.append("H")
            new = map[posy][posx]


        elif new == "I":
            print("U","U","U","X","U")
            print("U","U","X","O","X")
            print("U","U","U","X","U")
            print("U","U","U","U","U")
            print("U","U","U","E","U")
            list.append("I")
            new = map[posy][posx]


        elif new == "J":
            print("U","U","U","U","X")
            print("U","U","U","X","O")
            print("U","U","U","U","X")
            print("U","U","U","U","U")
            print("U","U","U","E","U")
            list.append("J")
            new = map[posy][posx]





        if new == "K":
            print("U","U","U","U","U")
            print("X","U","U","U","U")
            print("O","X","U","U","U")
            print("X","U","U","U","U")
            print("U","U","U","E","U")
            list.append("K")
            new = map[posy][posx]


        elif new == "L":
            print("U","U","U","U","U")
            print("U","X","U","U","U")
            print("X","O","X","U","U")
            print("U","X","U","U","U")
            print("U","U","U","E","U")
            list.append("L")
            new = map[posy][posx]


        elif new == "M":
            print("U","U","U","U","U")
            print("U","U","X","U","U")
            print("U","X","O","X","U")
            print("U","U","X","U","U")
            print("U","U","U","E","U")
            list.append("M")
            new = map[posy][posx]


        elif new == "N":
            print("U","U","U","U","U")
            print("U","U","U","X","U")
            print("U","U","X","O","X")
            print("U","U","U","X","U")
            print("U","U","U","E","U")
            list.append("N")
            new = map[posy][posx]


        elif new == "O":
            print("U","U","U","U","U")
            print("U","U","U","U","X")
            print("U","U","U","X","O")
            print("U","U","U","U","X")
            print("U","U","U","E","U")
            list.append("O")
            new = map[posy][posx]






        if new == "P":
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("X","U","U","U","U")
            print("O","X","U","U","U")
            print("X","U","U","E","U")
            list.append("P")
            new = map[posy][posx]


        elif new == "Q":
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","X","U","U","U")
            print("X","O","X","U","U")
            print("U","X","U","E","U")
            list.append("Q")
            new = map[posy][posx]


        elif new == "R":
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","X","U","U")
            print("U","X","O","X","U")
            print("U","U","X","E","U")
            list.append("R")
            new = map[posy][posx]


        elif new == "S":
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","X","U")
            print("U","U","X","O","X")
            print("U","U","U","E","U")
            list.append("S")
            new = map[posy][posx]


        elif new == "T":
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","X")
            print("U","U","U","X","O")
            print("U","U","U","E","X")
            list.append("T")
            new = map[posy][posx]






        if new == "U":
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("X","U","U","U","U")
            print("O","X","U","E","U")
            list.append("U")
            new = map[posy][posx]


        elif new == "V":
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","X","U","U","U")
            print("X","O","X","E","U")
            list.append("V")
            new = map[posy][posx]


        elif new == "W":
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","X","U","U")
            print("U","X","O","E","U")
            list.append("W")
            new = map[posy][posx]


        elif new == "X":
            posy = 0
            posx = 3
            new1 = map1[posy][posx]
            new = 0            
        elif new == "Y":
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","X")
            print("U","U","U","E","O")
            list.append("X")
            new = map[posy][posx]





        if new1 == "A":
            print("O","X","U","E","U")
            print("E","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","E")
            print("U","U","U","U","U")
            list.append("A")
            new1 = map1[posy][posx]


        elif new1 == "B":
            print("X","O","X","E","U")
            print("E","X","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","E")
            print("U","U","U","U","U")
            list.append("B")
            new1 = map1[posy][posx]


        elif new1 == "C":
            print("U","X","O","E","U")
            print("E","U","X","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","E")
            print("U","U","U","U","U")
            list.append("C")
            new1 = map1[posy][posx]


        elif new1 == "D":
            print("U","U","X","E","X")
            print("E","U","U","X","U")
            print("U","U","U","U","U")
            print("U","U","U","U","E")
            print("U","U","U","U","U")
            list.append("D")
            new1 = map1[posy][posx]


        elif new1 == "E":
            print("U","U","U","E","O")
            print("E","U","U","U","X")
            print("U","U","U","U","U")
            print("U","U","U","U","E")
            print("U","U","U","U","U")
            list.append("E")
            new1 = map1[posy][posx]






        if new1 == "F":
            print("X","U","U","E","U")
            print("E","X","U","U","U")
            print("X","U","U","U","U")
            print("U","U","U","U","E")
            print("U","U","U","U","U")
            list.append("F")
            new1 = map1[posy][posx]


        elif new1 == "G":
            print("U","X","U","E","U")
            print("E","O","X","U","U")
            print("U","X","U","U","U")
            print("U","U","U","U","E")
            print("U","U","U","U","U")
            list.append("G")
            new1 = map1[posy][posx]


        elif new1 == "H":
            print("U","U","X","E","U")
            print("E","X","O","X","U")
            print("U","U","X","U","U")
            print("U","U","U","U","E")
            print("U","U","U","U","U")
            list.append("H")
            new1 = map1[posy][posx]


        elif new1 == "I":
            print("U","U","U","E","U")
            print("E","U","X","O","X")
            print("U","U","U","X","U")
            print("U","U","U","U","E")
            print("U","U","U","U","U")
            list.append("I")
            new1 = map1[posy][posx]


        elif new1 == "J":
            print("U","U","U","E","X")
            print("E","U","U","X","O")
            print("U","U","U","U","X")
            print("U","U","U","U","E")
            print("U","U","U","U","U")
            list.append("J")
            new1 = map1[posy][posx]






        if new1 == "K":
            print("U","U","U","E","U")
            print("E","U","U","U","U")
            print("O","X","U","U","U")
            print("X","U","U","U","E")
            print("U","U","U","U","U")
            list.append("K")
            new1 = map1[posy][posx]


        elif new1 == "L":
            print("U","U","U","E","U")
            print("E","X","U","U","U")
            print("X","O","X","U","U")
            print("U","X","U","U","E")
            print("U","U","U","U","U")
            list.append("L")
            new1 = map1[posy][posx]


        elif new1 == "M":
            print("U","U","U","E","U")
            print("E","U","X","U","U")
            print("U","X","O","X","U")
            print("U","U","X","U","E")
            print("U","U","U","U","U")
            list.append("M")
            new1 = map1[posy][posx]


        elif new1 == "N":
            print("U","U","U","E","U")
            print("E","U","U","X","U")
            print("U","U","X","O","X")
            print("U","U","U","X","E")
            print("U","U","U","U","U")
            list.append("N")
            new1 = map1[posy][posx]


        elif new1 == "O":
            print("U","U","U","E","U")
            print("E","U","U","U","X")
            print("U","U","U","X","O")
            print("U","U","U","U","E")
            print("U","U","U","U","U")
            list.append("O")
            new1 = map1[posy][posx]






        if new1 == "P":
            print("U","U","U","E","U")
            print("E","U","U","U","U")
            print("X","U","U","U","U")
            print("O","X","U","U","E")
            print("X","U","U","U","U")
            list.append("P")
            new1 = map1[posy][posx]


        elif new1 == "Q":
            print("U","U","U","E","U")
            print("E","U","U","U","U")
            print("U","X","U","U","U")
            print("X","O","X","U","E")
            print("U","X","U","U","U")
            list.append("Q")
            new1 = map1[posy][posx]


        elif new1 == "R":
            print("U","U","U","E","U")
            print("E","U","U","U","U")
            print("U","U","X","U","U")
            print("U","X","O","X","E")
            print("U","U","X","U","U")
            list.append("V")
            new1 = map1[posy][posx]


        elif new1 == "S":
            print("U","U","U","E","U")
            print("E","U","U","U","U")
            print("U","U","U","X","U")
            print("U","U","X","O","E")
            print("U","U","U","X","U")
            list.append("W")
            new1 = map1[posy][posx]


        elif new1 == "T":
            print("U","U","U","E","U")
            print("E","U","U","U","U")
            print("U","U","U","U","X")
            print("U","U","U","X","E")
            print("U","U","U","U","X")
            list.append("X")
            print(True)
            new1 = map1[posy][posx]





        if new1 == "U":
            print("U","U","U","E","U")
            print("E","U","U","U","U")
            print("U","U","U","U","U")
            print("X","U","U","U","E")
            print("O","X","U","U","U")
            list.append("A")
            new1 = map1[posy][posx]


        elif new1 == "V":
            print("U","U","U","E","U")
            print("E","U","U","U","U")
            print("U","U","U","U","U")
            print("U","X","U","U","E")
            print("X","O","X","U","U")
            list.append("B")
            new1 = map1[posy][posx]


        elif new1 == "W":
            print("U","U","U","E","U")
            print("E","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","X","U","E")
            print("U","X","O","X","U")
            list.append("C")
            new1 = map1[posy][posx]


        elif new1 == "X":
            print("U","U","U","E","U")
            print("E","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","X","E")
            print("U","U","X","O","X")
            list.append("D")
            new1 = map1[posy][posx]


        elif new1 == "Y":
            print("U","U","U","E","U")
            print("E","U","U","U","U")
            print("U","U","U","U","U")
            print("U","U","U","U","E")
            print("U","U","U","X","O")
            new1 = map1[posy][posx]





        play = input("")
        if play == "d":
            if posx != 4:
                posx+=1
            else:
                continue
        elif play == "s":
            if posy != 4:
                posy+=1
            else:
                continue
        elif play == "a":
            if posx != 0:
                posx+=-1
            else:
                continue
        elif play == "w":
            if posy != 0:
                posy+=-1
            else:
                continue
        print (number)
        print("HI")

