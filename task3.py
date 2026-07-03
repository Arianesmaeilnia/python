student_scores = [18,9,14,11,8,20,10]

passed = []
failed = []

for student_score in student_scores:
    if student_score >=10:
        passed.append(student_score)
    else : failed.append(student_score)

print(len(passed))
print(failed)