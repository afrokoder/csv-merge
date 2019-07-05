i=1
while i < 6:
    print (i)
    i+=1


fruits = ["apple", "banana","cherry"]
for x in fruits:
    print(x)


for x in range(6):
        print(x)


print("for incrementing")
for outer_loop in range (1,10):
    for inner_loop in range(1,10):
        if inner_loop < outer_loop +1:
            print(outer_loop, end="")
    print()
print("for decrementing")
for outer_loop in range (9,0,-1):
    for inner_loop in range(9,0,-1):
        if inner_loop <= outer_loop:
            print(outer_loop, end="")
    print()