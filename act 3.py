# number greater than 50 and even
 
number=int(input("enter a number"))

if number>50:
    print(number, "greater than 50")
    if number%2==0:
        print("and the number is even")
    else:
        print("and the number is odd")
else:
    print(number,"is less than 50")
