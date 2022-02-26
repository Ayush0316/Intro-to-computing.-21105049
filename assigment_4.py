# Question 01.
print("\t Question 01 \n")

# Recursive function for tower of honie problem.
def tower_of_honie(number_of_dics,a,b,c):
    if number_of_dics > 0:
        tower_of_honie(number_of_dics -1, a, c, b)
        print(f"Move disc {number_of_dics} from {a} to {c}")
        tower_of_honie(number_of_dics -1, b,a,c)

# Inilising the number of dics and calling the function.
number_of_dics = 3  # As per the question 
tower_of_honie(3, "a", 'b', 'c')  # Here a is the strating tower ,b is the helping tower and c is the ending tower.
print()


# Question 02
print("\t Question 02 \n")

# Using Recurrsion.
print("Using recurrsion. \n")

# Recursive function for pascal's triangle.
def pascel_triangle(n,list1):             # n is the number of lines to print.
    if n == 0 :
        return
    
    pascel_triangle(n-1,list1)       # Calling function again for recurrsion.

    l = len(list1)
    list2 = list1.copy()             
    list1.append(1)

    for counter in range(0,l):              # Using for loop to get the next line.
        if counter == 0:
            list1[0] = 1
        else:
            list1[counter] = list2[counter] + list2[counter-1]
    
    proper_pattern(list1)                # Calling function to print the triangle.


# Function to print pascal's traiangle in proper manner.
def proper_pattern(list1):
    print(" "*(number - len(list1)), end = "")

    for item in list1:
        print(item , end = " ")
    print()
    
# Asking for number of line to print.
number = int(input("Enter the number(natural number) of line to print: "))
print()

# Calling recursive function to generate the pascal's traingle.
initial_list = []
pascel_triangle(number,initial_list)


# Using iteration.
print("\n Using iteration.\n")

output_list = []

for counter in range(number):
    if len(output_list) == 0:
        temp_list = []
    else:
        temp_list = output_list[counter - 1].copy()

    temp_list.append(1)
    
    if counter > 1:
        for j in range(1,len(output_list[counter - 1])):
            temp_list[j] = output_list[counter - 1][j] + output_list[counter - 1][j - 1]

    output_list.append(temp_list)

for lst in output_list:
    proper_pattern(lst)



# Question 3.
print("\n\t Question 3 \n")

# Asking for two numbers from the user.
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter second number(number must not be zero): "))
print()

# Using inbuilt function to calculate quotient and reminder.
quotient_reminder = divmod(num_1, num_2)
print(f"The quotient and reminder of the values are {quotient_reminder}")


print("\n\tPart A\n")

# Checking whether the object is callable or not.
check = callable(quotient_reminder)
if check == True:
    print("It is callable.")
elif check == False:
    print("It is not callable.")


print("\n\t Part B\n")

# Checking whether the values are non zero or not.
if quotient_reminder == (0,0):
    print("Both values are zero.")
elif quotient_reminder[0] == 0:
    print("Only quotient is zero")
elif quotient_reminder[1] == 0:
    print("Only reminder is zero.")
else:
    print("Both are non zero.")


print("\n\t Part C \n")

# Adding values to the previous set.
new_result = quotient_reminder.__add__((4,5,6))
print(f"Result after adding values: {new_result} \n")

# Filtering out the values greater than 4 in a list.
list_after_removing_value_greater_than_4 = []
for counter in range(len(new_result)):
    if new_result[counter] <= 4:
        list_after_removing_value_greater_than_4.append(new_result[counter])
print(f"List after removing value greater than 4: {list_after_removing_value_greater_than_4}")
print()


print("\n\t Part D \n")

# Converting list of values greater than 4 into a set.
converting_to_set = set(list_after_removing_value_greater_than_4)
print(f"After converting the above result into set {converting_to_set} \n")


print("\n\t Part E \n")

# Making the set immutable.
converting_to_immutable = frozenset(converting_to_set)
print("Now set is immutable")

print("\n\t Part f \n")

# Calculating the max value and hash value.
print(f"Max value in the set is {max(converting_to_immutable)}")
print(f"Hash value is: {hash(converting_to_immutable)}")

# Question 4.
print("\n\t Question 4 \n")

# Creating class named student.
class Student():

    # Using init function to initilize name and roll number.
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        print(f"Object created for {self.name}")

    # Defining a function to show deatails of the student.
    def show_info(self):
        print(f'The name of the student is {self.name}')
        print(f'The roll number of {self.name} is {self.rollno}')

    # Defining destructor.
    def __del__(self):
        print(f"Destructor deleted {self.name}'s record.")

# Creating objects to class student.
student_1 = Student("Ayush kansal", 21105049)
student_2 = Student("Namit kulshreshtra", 21105025)
student_3 = Student("Harmanpreet singh", 21105053)
print()

# Using class function to show deatials of student.
student_1.show_info()
print("\n")
student_2.show_info()
print("\n")
student_3.show_info()
print('\n')

# Calling destructor.
del student_1
del student_2
del student_3

# Question 5
print("\n\t Question 05\n")

# Creating a class names factory.
class factory():

    # Using init function to store data of the employee.
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"Object created named {self.name}.")

    # Defining a function to show data of the employee.
    def show_info(self):
        print("\tShowing info of the employee.")
        print(f"Name of the employee working in this factory is {self.name}")
        print(f"Salary of {self.name} is {self.salary}.")

    # Defining a function to update the salary of the employee.
    def update_salary(self,new_salary):
        self.salary = new_salary
        print(f"Updated salary of the employee {self.name} is {self.salary}\n")

    # Defining destructor to delete the data of the employee.
    def __del__(self):
        print(f"Record of the employee {self.name} is deleted.")
    
# Crating objects of the class factory.
Mehak = factory('Mehak', 40000)
Ashok = factory("Ashok", 50000)
Viren = factory('Viren', 60000)
print()

# Calling function to show the data of the employee.
Mehak.show_info()
print()
Ashok.show_info()
print()
Viren.show_info()
print()

# Calling a function to update the salary of the employee.
print("Updating mehak's salary.")
Mehak.update_salary(70000)

# Calling destructor to remove data of the employee
print("Calling destructor to delete viren's record.")
del Viren

# Question 6 
print("\n\t Question 6 \n")

# Taking inputs from the friends.
utter_word = input("Frist friend please enter the uttered word: ")
print()
new_word = input("Friend 2 please enter new word to test your friendship: ")
print()

# Inilizing two lists to count the letters.
count_list_uttered_word = [0]*26
count_list_new_word = [0]*26

# Counting occurance of each letter for uttered word.
for letter in utter_word:
    count_list_uttered_word[ord(letter.lower()) - ord('a')] += 1

# Counting occurance of each letter for new word.
for letter in new_word:
    count_list_new_word[ord(letter.lower()) - ord('a')] += 1

# Checking whether both the counting lists are same or not.
if count_list_uttered_word == count_list_new_word:

    while True:

        # Asking shopkepper whether the new word have some meaning or not and print the result accordingly.
        check = input("Please enter whether the new word have meaning or not(Y or N): ")
        print()
        if check == "Y":
            print("You and your friend passed the friendship test.")
            break
        elif check == "N":
            print("Oops! You and your friend failed the friendship test")
            break
        else:
            print("Please enter a valid input.(Y or N)")

# Printing result if both the list dont match.
else:
    print("Oops! You and your friend failed the friendship test")