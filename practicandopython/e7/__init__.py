first_evaluation_grade = float(input("Enter the grade for the first evaluation: "))
second_evaluation_grade = float(input("Enter the grade for the second evaluation: "))
third_evaluation_grade = float(input("Enter the grade for the third evaluation: "))

weight_first_evaluation = 0.30
weight_second_evaluation = 0.40
weight_third_evaluation = 0.30

average_grade = (first_evaluation_grade * weight_first_evaluation +
                second_evaluation_grade * weight_second_evaluation +
                third_evaluation_grade * weight_third_evaluation)

print(f"The course's average grade is: {average_grade:.2f}")
