# Solution 1.

print("Solution 1.")

# Asking for numbers from the user.
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

# Calculating the average of numbers.
average = (num_1 + num_2 + num_3) / 3.0

# Printing the numbers.
print("Average of numbers entered by use is: " , average)
print()
# Solution 2.

print("Solution 2.")

#  Asking for income and number of dependents.
gross_income = float(input("Enter income to the nearest penny: $"))
num_of_dependents = int(input("Enter number of dependents: "))

#  Initializing the variables.
tax_rate = 0.20
standard_deduction = 10000
dependent_deduction = 3000

# Calculating the Tax.
taxable_income = gross_income - standard_deduction - (dependent_deduction * num_of_dependents)
tax = taxable_income * tax_rate

# Printing tax.
if tax < 0:
    print("Your incone tax is $0")
else:
    print("Your incone tax is $" , tax)
print()

# Solution 3.

print("Solution 3.")

# Asking for deatials.
SID = int(input("Enter your SID: "))
Name = input("Enter your name: ")
Gender = input("Enter your gender: ")
Course_name = input("Enter your course name: ")
CGPA = float(input("Enter your CGPA: "))

# Making a list having different datatypes.
student = [SID , Name , Gender , Course_name , CGPA]

# Printing list.
print("List containing different datatypes is: " , student)
print()
# Solution 4.

print("Solution 4.")

# Asking for marks.
Student_1_marks = float(input("Enter student 1 marks: "))
Student_2_marks = float(input("Enter student 2 marks: "))
Student_3_marks = float(input("Enter student 3 marks: "))
Student_4_marks = float(input("Enter student 4 marks: "))
Student_5_marks = float(input("Enter student 5 marks: "))

# Making a list.
Marks = [ Student_1_marks , Student_2_marks , Student_3_marks , Student_4_marks , Student_5_marks]

# Sorting the list.
Marks.sort()

# Printing sorted list of marks.
print("Sorted list of students marks: " , Marks)
print()

# Solution 5.

# Inilising the list.
Colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Solution 5.a
print("Solution 5.a")
Colour.pop(3)
print("List after removing 4th element: ", Colour)
print()

# Solution 5.b
Colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Solution 5.b")
Updated = ["Purple" if (x == 'Black' or x == 'Pink') else x for x in Colour]
print("List after replacing Black and Pink with Purple: " , Updated)
