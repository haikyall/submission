student_scores = {
	"Alice" : [85, 90, 92],
	"Bob" : [78, 80, 85],
	"Charlie" : [92, 88, 95] 
}

student_grade1= student_scores['Alice']
student_grade2= student_scores['Bob']
student_grade3= student_scores['Charlie']

#for grade in student_grade:
	#print(grade)

for student, grades in student_scores.items():
	print(f'{student} =',*grades)
