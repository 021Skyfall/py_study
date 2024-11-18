total_grade = 0.0
total_credits = 0.0

while True:
    try:
        line = input()
        arr = line.split()

        # 학점 기준 설정
        if arr[2] == "A+":
            standard = 4.5
        elif arr[2] == "A0":
            standard = 4.0
        elif arr[2] == "B+":
            standard = 3.5
        elif arr[2] == "B0":
            standard = 3.0
        elif arr[2] == "C+":
            standard = 2.5
        elif arr[2] == "C0":
            standard = 2.0
        elif arr[2] == "D+":
            standard = 1.5
        elif arr[2] == "D0":
            standard = 1.0
        elif arr[2] == "P":
            arr[1] = "0"
            standard = 0.0
        else:
            standard = 0.0

        cre = float(arr[1])
        total_credits += cre
        total_grade += cre * standard

    except EOFError:
        break

# 평균 학점 계산
if total_credits > 0:
    average_grade = total_grade / total_credits
else:
    average_grade = 0.0

print(average_grade)