from sys import exit

# Values
a = ["0","1","2","3","4","5","6","7","8","9"]

#start x or o

s1 = ""
s2 = ""

start = input(f"O or X: ")

if start == "X" or start == "x":
    s1 = "X"
    s2 = "O"
elif start == "O" or start == "o":
    s1 = "O"
    s2 = "X"


# the game 
print()
print(a[1],"|",a[2],"|",a[3])
print("—————————")
print(a[4],"|",a[5],"|",a[6])
print("—————————")
print(a[7],"|",a[8],"|",a[9])
print()


# if win
def s1win():
    if a[1] == s1 and a[2] == s1 and a[3] == s1:
        print(f"Congratulations, {s1} won")
        exit()
    elif a[4] == s1 and a[5] == s1 and a[6] == s1:
        print(f"Congratulations, {s1} won")
        exit()
    elif a[7] == s1 and a[8] == s1 and a[9] == s1:
        print(f"Congratulations, {s1} won")
        exit()
    elif a[1] == s1 and a[4] == s1 and a[7] == s1:
        print(f"Congratulations, {s1} won")
        exit()
    elif a[2] == s1 and a[5] == s1 and a[8] == s1:
        print(f"Congratulations, {s1} won")
        exit()
    elif a[3] == s1 and a[6] == s1 and a[9] == s1:
        print(f"Congratulations, {s1} won")
        exit()
    elif a[1] == s1 and a[5] == s1 and a[9] == s1:
        print(f"Congratulations, {s1} won")
        exit()
    elif a[7] == s1 and a[5] == s1 and a[3] == s1:
        print(f"Congratulations, {s1} won")
        exit()

def s2win():
    if a[1] == s2 and a[2] == s2 and a[3] == s2:
        print(f"Congratulations, {s2} won")
        exit()
    elif a[4] == s2 and a[5] == s2 and a[6] == s2:
        print(f"Congratulations, {s2} won")
        exit()
    elif a[7] == s2 and a[8] == s2 and a[9] == s2:
        print(f"Congratulations, {s2} won")
        exit()
    elif a[1] == s2 and a[4] == s2 and a[7] == s2:
        print(f"Congratulations, {s2} won")
        exit()
    elif a[2] == s2 and a[5] == s2 and a[8] == s2:
        print(f"Congratulations, {s2} won")
        exit()
    elif a[3] == s2 and a[6] == s2 and a[9] == s2:
        print(f"Congratulations, {s2} won")
        exit()
    elif a[1] == s2 and a[5] == s2 and a[9] == s2:
        print(f"Congratulations, {s2} won")
        exit()
    elif a[7] == s2 and a[5] == s2 and a[3] == s2:
        print(f"Congratulations, {s2} won")
        exit()


#game start
        
for n in range(0,9):
    
    if n == 0 or n == 2 or n == 4 or n == 6 or n == 8: 
        step = int(input(f"It is the turn of the '{s1}' : "))
        a[step] = s1
    elif n == 1 or n == 3 or n == 5 or n == 7 or n == 9:
        step = int(input(f"It is the turn of the '{s2}' : "))
        a[step] = s2


    
    print()
    print(a[1],"|",a[2],"|",a[3])
    print("—————————")
    print(a[4],"|",a[5],"|",a[6])
    print("—————————")
    print(a[7],"|",a[8],"|",a[9])
    print()

    s1win()
    s2win()

