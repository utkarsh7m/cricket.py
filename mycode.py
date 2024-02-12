import random
h=0
k=0
d=0
e=0
r=0
i = str
j = str
randno1 = random.randint(0,5)
if randno1 == 0:
    comp = "even"
elif randno1 == 1:
    comp = "odd"
elif randno1 == 2:
    comp = "even"
elif randno1 == 3:
    comp = "odd"
elif randno1 == 4:
    comp = "even"
elif randno1 == 5:
    comp = "odd"


a = int(input("choose any no. between 0-5(odd or even?): "))


b = a % 2
if b == 0:
    print("your no. = even")
    c = "even"
else:
    print("your no. = odd")
    c = "odd"
print(f"computer no. is {randno1} which is {comp}")

# comparision between comp and user
if comp == "odd" and c == "odd":
    print("As odd + odd = even")
    print("you lose the toss.")
    d = False
elif comp == "even" and c == "odd":
    print("As odd + even = odd")
    print("you won the toss.")
    d = True
elif comp == "odd" and c == "even":
    print("As even + odd = odd")
    print("you lose the tose.")
    d = False
elif comp == "even" and c == "even":
    print("As even + even = even")
    print("you won the tose.")
    d = True
# end of stage 1


randno2 = random.randrange(1,2)
if randno2 == 1:
    comp1 = "Bat"
    comp2 = "Batting"
elif randno2 == 2:
    comp1 = "Ball"
    comp2 = "Balling"

if d == True:
    print("-------------------------------")
    e = input("Choose bat or ball?: ")
elif d == False:
    print("-------------------------------")
    print(f"Computer choose to {comp1} first.")

# your batting code
if comp1 == "Ball" or e =="bat":
    x = 25
    i = "Computer"
    j = "User"
    print("Time for your batting")
    while True:    
        print("Choose between 1 to 5 only")
        g = int(input("Your Batting:"))
        f = random.randint(1,5)
        print(f"Computer chooses {f}")
        if g == f:
            break
        h = h + g
        d = h
        print(f"User Run : {d}")
        print("-------------------------------")
    print(f"{j} is Out")
    print(f"{j} score is {d}")
    print("-------------------------------")
    print(f"Now {i} {comp2} :")
# computer batting
elif comp1 == "Bat" or e=="ball":
    x = 30
    i = "Computer"
    j = "User"
    print("Time for your balling")
    while True:
        print("Choose between 1 to 5 only")
        g = int(input("Your Balling:"))
        f = random.randint(1,5)
        print(f"Computer chooses {f}")
        if g == f:
            break
        h = h + f
        k = h
        print(f"Comp Run : {k}")
        print("-------------------------------")
    print(f"{i} is Out")
    print(f"{i} score is {k}")
    print("-------------------------------")
    print(f"Now {j} {comp2} :")

# user balling
if x == 25:
    j = "Computer"
    while True:
        g = int(input("Enter the number(between:1-5):"))
        f = random.randint(1,5)
        print(f"Computer chooses {f}")
        if g == f:
            break
        r = r + f
        k = r
        print(f"Total : {k}")
        print("-------------------------------")
    print(f"{j} is Out")
    print(f"{j} score is {k}")
    print("----------------------------------")
    print(f"User Total Score : {d}")
    print(f"Computer Total Score : {k}")
    print("-------------------------------")
    if d > k:
        print(f"YOU WON THE MATCH BY {d-k} RUNS")
        print("PARTY CHAHIYE ABB")
    else:
        print(f"YOU LOSE BY {k-d} RUNS :(")
        print("TRY AGAIN, DON'T GIVE UP ;)")
# user batting
elif x == 30:
    i = "User"
    while True:
        g = int(input("Enter the number(between:1-5):"))
        f = random.randint(1,5)
        print(f"Computer chooses {f}")
        if g == f:
            break
        r = r + g
        d = r
        print(f"Total : {d}")
        print("-------------------------------")
    print(f"{i} is Out")
    print(f"{i} score is {d}")
    print("-------------------------------")
    print(f"User Total Score : {d}")
    print(f"Computer Total Score : {k}")
    print("-------------------------------")
    if k < d:
        print(f"YOU WON THE MATCH BY {d-k} RUNS")
        print("PARTY CHAHIYE ABB")
    else:
        print(f"YOU LOSE BY {k-d} RUNS :(")
        print("TRY AGAIN, DON'T GIVE UP ;)")