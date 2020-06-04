
def grade_calc(hw_score, asm_score, fa_score):
    
    total_mark = hw_score + asm_score + fa_score
    
    if total_mark >=150:
        grade = "A"
    elif total_mark >=125:
        grade = 'B'
    elif total_mark >=100:
        grade = 'C'
    elif total_mark >=75:
        grade = 'D'
    elif total_mark >=50:
        grade = 'E'
    else:
        grade = 'F'
    
    return grade

student_name = input("What is the student's name?")

hw_score = int(input("What was " + student_name +"'s homework score?:"))
asm_score = int(input("What was " + student_name +"'s assessment score?:"))
fa_score = int(input("What was " + student_name +"'s final exam score?:"))

final_grade = grade_calc(hw_score, asm_score, fa_score)
        
print(student_name +"'s final grade is " + final_grade)
