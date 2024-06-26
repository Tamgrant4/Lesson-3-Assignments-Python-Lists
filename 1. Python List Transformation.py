# Q1 Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the grades in descending order using the built-in sort method with reverse=True
grades.sort(reverse=True)

# Print the sorted grades
print(grades)

#Task 2

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the grades in descending order (already done in previous step)
# grades.sort(reverse=True)  # Uncomment this line if you want to sort again

# Calculate the average grade
total_grades = sum(grades)
average_grade = total_grades / len(grades)
# Print the average grade
print(f"The average grade is: {average_grade:.2f}")

#Task 3

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the grades in descending order (already done in previous step)
# grades.sort(reverse=True)  # Uncomment this line if you want to sort again

# Calculate the average grade
total_grades = sum(grades)
average_grade = total_grades / len(grades)

# Print the average grade
print(f"The average grade is: {average_grade:.2f}")

# Replace grades below 80 with "Failed"
for i in range(len(grades)):
  if grades[i] < 80:
    grades[i] = "Failed"

# Print the modified grades
print("\nGrades after replacing:")
for grade in grades:
  print(grade)

  # Q2 Task 1

  submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find the intersection of the two lists (students who are in both lists)
present_in_both = set(submitted) & set(attended)

# Print the names of students who attended and submitted assignments
print("Students who attended the class and submitted assignments:")
for name in present_in_both:
  print(name)

  #Task 2

  submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Check if the two lists have the same elements (regardless of order)
is_identical = sorted(submitted) == sorted(attended)

if is_identical:
  print("The two lists are identical in terms of content.")
else:
  print("The two lists are not identical in terms of content.")

#Task 3

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Efficiently remove students from attended who are not in submitted using list comprehension
attended = [student for student in attended if student in submitted]

print("Students who attended and submitted assignments:", attended)

# Q3 Task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Assuming there are 30 days in a month, calculate the starting index for the second week (7 days)
second_week_start_index = 7

# Extract the temperatures for the second week using slicing
second_week_temperatures = temperatures[second_week_start_index:second_week_start_index + 7]

print("Temperatures for the second week:", second_week_temperatures)

#Task 2

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Use list comprehension to create a new list containing temperatures above 100
high_temperatures = [temp for temp in temperatures if temp > 100]

print("Temperatures above 100:", high_temperatures)

#Task 3

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Reverse the temperatures list
reversed_temperatures = temperatures[::-1]

# Extract temperatures from the 5th to 10th day (inclusive) of the reversed list using slicing
# Since indexing starts from 0, adjust indices to match the desired range
fifth_to_tenth_day_temperatures = reversed_temperatures[4:10]  

print("Temperatures from the 5th to 10th day (reversed list):", fifth_to_tenth_day_temperatures)

# Q4 Task 1

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Filter students with grades above or equal to 80 (using list comprehension)
passed_students = [student for student, grade in zip(students, grades) if grade >= 80]
passed_students_grades = [grade for grade in grades if grade >= 80]
passed_students_activities = [activity for activity in activities if grades[activities.index(activity)] >= 80]  # Match activities to students who passed

# Print information for students who passed
for i in range(len(passed_students)):
  print(passed_students[i], passed_students_grades[i], passed_students_activities[i])

#Task 2

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Filter students with grades above or equal to 80
students_approved = [student for student, grade in zip(students, grades) if grade >= 80]

# Print the list of approved students
print("Students who passed (approved):", students_approved)

#Task 3

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Filter students with grades above or equal to 80
students_approved = [student for student, grade in zip(students, grades) if grade >= 80]

# Print the list of approved students
print("Students who passed (approved):", students_approved)
