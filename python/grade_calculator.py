"""
A Python program to calculate and format grades.
Author: Fritz
Course: Software Engineering Bootcamp
Date: [Date of last modification]
Description: This program calculates the average and final letter grades based on user-inputted grades.
"""

class Student:
    """Class representing a student and their associated grade calculations."""
    def __init__(self, name="Student"):
        self.name = name

    def get_name(self):
        return self.name

class GradeCalculator:
    """Class responsible for calculating the sum, number, and average of grades."""
    def __init__(self):
        self.total_grades = 0
        self.grade_count = 0

    def add_grade(self, grade):
        """Adds a grade to the running total and increments the grade count."""
        self.total_grades += grade
        self.grade_count += 1

    def calculate_average(self):
        """Calculates the average of all grades, rounded to one decimal place."""
        if self.grade_count == 0:
            return 0.0
        return round(self.total_grades / self.grade_count, 1)
    
    def get_letter_grade(self):
        """Determines the letter grade based on the average of the grades."""
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif 80 <= average < 90:
            return 'B'
        elif 70 <= average < 80:
            return 'C'
        elif 60 <= average < 70:
            return 'D'
        else:
            return 'F'

def main():
    """Main function to execute the program logic."""
    student_name = input("Enter the student's name: ")
    student = Student(student_name)

    num_grades = int(input("Enter the number of grades: "))

    grade_calculator = GradeCalculator()

    for i in range(num_grades):
        grade = float(input(f"Enter grade {i + 1}: "))
        grade_calculator.add_grade(grade)

    average = grade_calculator.calculate_average()
    letter_grade = grade_calculator.get_letter_grade()

    # Print only the class average and final letter grade
    print("*********************************")
    print("Grade report for: ", student.get_name())
    print(f"The class average is: {average:.2f}")
    print(f"The final letter grade: {letter_grade}")


if __name__ == "__main__":
    main()