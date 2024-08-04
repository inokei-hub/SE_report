# プログラムの説明:
# このプログラムは、複数の学生の成績を管理し、合計点と平均点を計算し、
# 最も成績の良い学生を見つけます。

# 学生の成績のリストから合計点と平均点を計算
def calculate_total_and_average(grades):
    
    total = sum(grades)
    average = total / len(grades)
    return total, average

# 全ての学生の中から最も成績の良い学生を探索
def find_top_student(students):
    
    max_total = 0
    top_student = ""
    
    for student, grades in students.items():
        total, average = calculate_total_and_average(grades)
        if total > max_total:
            max_total = total
            top_student = student
        print(f"Student: {student}, Total: {total}, Average: {average:.2f}")
    
    return top_student, max_total

students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [70, 75, 80],
    "David": [95, 85, 90]
}

top_student, top_score = find_top_student(students)
print(f"Best student: {top_student} with total score: {top_score}")
