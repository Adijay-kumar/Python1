a = int(input("Enter the number you want to check is it prime or not: "))
for i in range(2,a):
    if a%i != 0:
        print("Yes",a,"is a Prime number")
        break
    else:
        print("No",a,"is not a Prime number")
        break
