# WAP to display grading system with four subjects.

marks1 = int(input("Enter marks in Maths : "))
marks2 = int(input("Enter marks in English : "))
marks3 = int(input("Enter marks in Physics : "))
marks4 = int(input("Enter marks in Chemistry : "))

total = marks1 + marks2 + marks3 + marks4
percentage = total / 4

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print(f"marks1 : {marks1}")
print(f"marks2 : {marks2}")
print(f"marks3 : {marks3}")
print(f"marks4 : {marks4}")
print(f"Total : {total}")
print(f"Percentage : {percentage}%")
print(f"Grade : {grade}")
