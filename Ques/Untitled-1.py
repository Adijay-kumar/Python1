a = int(input("Enter the start number"))
b = int(input("Enter the end number"))
for i in range(a,b):
    for j in range(a,b):
        if i%j == 0 and i%1 == 0:
    print(i)