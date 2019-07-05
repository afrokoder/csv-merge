
outer_loop = 1

while outer_loop < 10:
    inner_loop = 1
    while inner_loop < outer_loop + 1:
        print (outer_loop, end="")
        inner_loop = inner_loop + 1


    print()
    outer_loop = outer_loop + 1


#outer_loop = 10
for outer_loop in range (9,0,-1):
    for inner_loop in range (9,0,-1):
        if inner_loop <= outer_loop:
            print(outer_loop, end="")
    print()
