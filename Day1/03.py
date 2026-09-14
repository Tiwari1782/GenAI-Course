# for i in range(1, 21, 2):
#     print(i)

# roll = [1,2,3,4,5,6,7,8,9,10]
# name = ["Liam","Emma",
#     "Noah",
#     "Olivia",
#     "Ethan",
#     "Sophia",
#     "Lucas",
#     "Ava",
#     "James",
#     "Mia"]
# courses = [
#     "Mathematics",
#     "Physics",
#     "Chemistry",
#     "Computer Science",
#     "Data Structures",
#     "Database Management",
#     "Operating Systems",
#     "Artificial Intelligence",
#     "Machine Learning",
#     "Web Development"
# ]

# for r, n , c in zip(roll, name, courses):
#     print(r, n, c)

# sum = 0
# product = 1
# for i in range(1,10):
#     sum+=i
#     product = product* i

# print(f"Sum is : {sum}")
# print(f"Product is : {product}")

# for i in range(1,22):
#     if( i % 2 == 0):
#         print(i)

# fibonacci series

# a = 0 
# b = 1

# for i in range(10):
#     print(a)
#     c = a + b
#     a = b
#     b = c

# Reverse num using while loop
num = int(input("Enter number: "))

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse:", rev)

# Armstrong num
num = int(input("Enter number: "))

original = num
sum = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# Prime num
num = int(input("Enter number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

# Palindrome num
num = int(input("Enter number: "))

original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")

    