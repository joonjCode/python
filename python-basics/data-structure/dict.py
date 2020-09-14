from collections import defaultdict

student_grades = {
	"Jack":[85, 90],
	"Jill":[80,95]
}

def get_grades_naive(name):
	if name in student_grades:
		return student_grades[name]
	return []

def get_grades_better(name):
	return student_grades.get(name, [])


def get_grades_with_assignment(name):
	if name not in student_grades:
		student_grades[names] = []

	return student_grades[name]

def get_grades_with_assignment_better(name):
	return student_grades.setdefault(name, [])

def set_grades_naive(name, score):
	if name in student_grades:
		grades = student_grades[name]
	else:
		student_grades[name]= []
		grades = student_grades[name]
	grades.append(score)

def set_grades_better(name, score):
	grades = get_grades_with_assignment_better(name)
	grades.append(score)

student_grades = defaultdict(list)

def set_grade_best(name, score):
	student_grades[name].append(score)