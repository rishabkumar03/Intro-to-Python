# GRADE CALCULATOR  
    # Assign a letter grade based on a student's score: A(90-100), B(80-99), C(70-79), D(60-69), F(below 60).

score = 101

if score >= 101:
    print("Please enter valid score")
    exit()

if score >= 90:
    grade = "A"    
elif score >= 80:
    grade = "B"   
elif score >= 70:
    grade = "C" 
elif score >= 60:
    grade = "D"   
else:
    grade = "F"

print("Grade", grade)