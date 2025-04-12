"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade. If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""
if __name__ == '__main__':
    # Read the number of students
    n = int(input())
    
    # Initialize an empty list to store student names and grades
    students = []
    
    # Read the names and grades of each student
    for _ in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])
    
    # Extract all grades from the list of students
    grades = [student[1] for student in students]

    # Remove duplicate grades and sort them in ascending order
    unique_grades = sorted(set(grades))
    
    # Find the second lowest grade
    second_lowest_grade = unique_grades[1]
    
    # Find the names of students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    # Print the names of students with the second lowest grade
    for student in second_lowest_students:
        print(student)
