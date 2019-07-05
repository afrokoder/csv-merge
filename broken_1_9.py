#Number half pyramid
#Makes a half pyramid of numbers up to 9
#1
#22
#333
#4444
#55555

#No errors here
outer_loop = 1

while outer_loop < 10:
    inner_loop = 1
    while inner_loop < outer_loop + 1:
        print (outer_loop, end="")
        inner_loop = inner_loop + 1


    print()
    outer_loop = outer_loop + 1


input("Press enter key:")
print("\n\n\n\n\n")
####################################################### End error free zone

#For Loop - print all odd numbers less than 10
print("All the odd numbers")
for odd_number in range(1, 12): #start at 0 end at 12
    if odd_number % 2!=0:
        print(odd_number)

print("\n\n\n\n")

#While Loop - print all even numbers less than 10
print("All the even numbers")
even_number = 2
while even_number < 9:     
        print(even_number)
        even_number = even_number  + 2

print("\n\n\n")


#Challenge - Flip the pyramid
#Make a half pyramid of numbers up to 9
#999999999
#88888888
#7777777
#666666
outer_loop = 10
while outer_loop <= 9 :
    inner_loop = 0
    while inner_loop < outer_loop - 1:
        print (outer_loop, end="")
        inner_loop = inner_loop - 1

    print()
    outer_loop = outer_loop - 1

print("\n\n\n")




