from random import randint
# com=randint(1,6)
com=[]
a=int(input("enter total number of dices to be roll"))
for i in range (0,a):
    com.append(randint(1,6))
print(com)
    
for j in range (0,len(com)):
    match com[j]:
        case 1:
            print(" ___ ")
            print("|   |")
            print("| • |")
            print("|   |")
            print(" ─── ")
        case 2:
            print(" ___ ")
            print("|•  |")
            print("|   |")
            print("|  •|")
            print(" ─── ")
        case 6:
            print(" ___ ")
            print("|• •|")
            print("|• •|")
            print("|• •|")
            print(" ─── ")
        case 3:
            print(" ___ ")
            print("|•  |")
            print("| • |")
            print("|  •|")
            print(" ─── ")
        case 4:
            print(" ___ ")
            print("|• •|")
            print("|   |")
            print("|• •|")
            print(" ─── ")
        case 5:
            print(" ___ ")
            print("|• •|")
            print("| • |")
            print("|• •|")
            print(" ─── ")
    
        