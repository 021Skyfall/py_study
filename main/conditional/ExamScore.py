# A = int(input())
#
# if A >= 90:
#     print("A")
# elif 80 <= A < 90:
#     print("B")
# elif 70 <= A < 80:
#     print("C")
# elif 60 <= A < 70:
#     print("D")
# else:
#     print("F")

def get_grade(X):
    grades = {
        'A': X >= 90,
        'B': 80 <= X < 90,
        'C': 70 <= X < 80,
        'D': 60 <= X < 70,
        'F': X < 60
    }
    for grades, condition in grades.items():
        if condition:
            return grades

A = int(input())
print(get_grade(A))