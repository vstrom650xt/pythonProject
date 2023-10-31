first_evaluation_grade = input("Did the student fail the first evaluation? (Y/N): ").upper()
second_evaluation_grade = input("Did the student fail the second evaluation? (Y/N): ").upper()
third_evaluation_grade = input("Did the student fail the third evaluation? (Y/N): ").upper()

if first_evaluation_grade == "Y" and second_evaluation_grade == "Y" and third_evaluation_grade == "Y":
    print("The student has failed all evaluations and cannot pass the course in the regular session.")
elif first_evaluation_grade == "N" or second_evaluation_grade == "N" or third_evaluation_grade == "N":
    print("The student has passed at least one of the evaluations and can pass the course in the regular session.")
else:
    print("The student has failed all evaluations but can still pass the course in the regular session because passing with the first evaluation failed is allowed.")
