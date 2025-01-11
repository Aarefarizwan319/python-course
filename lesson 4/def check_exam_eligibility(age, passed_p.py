def check_exam_eligibility(age, passed_prerequisite):
    if age >= 18 and passed_prerequisite:
        return "You are eligible to take the exam."
    else:
        return "You are not eligible to take the exam."

age = int(input("Enter your age: "))
prerequisite = input("Have you passed the prerequisite course? (yes/no): ").lower()

if prerequisite == "yes":
    passed_prerequisite = True
else:
    passed_prerequisite = False

eligibility_message = check_exam_eligibility(age, passed_prerequisite)
print(eligibility_message)
