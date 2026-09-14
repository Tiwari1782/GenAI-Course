a = int(input("Enter number : "))
b = float(input("Enter float val : "))

temp = a
a = b
b = temp

print("Swapped Values : ")
print(a)
print(b)


a = int(input("Enter number : "))
b = float(input("Enter float val : "))

a, b = b, a

print("Swapped Values : ")
print(a)
print(b)
