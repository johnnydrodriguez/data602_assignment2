
"""
Q1 What will the following code display? Can you debug and fix the output?
The code should return the entire list
"""


# Original code printed emtpy list.  Debugged by updating the index.
numbers = [1, 2, 3, 4, 5]
print(numbers[0:5])


"""
Q2  Design a program that asks the user to enter a store’s sales for each day of the
week. The amounts should be stored in a list. Use a loop to calculate the total sales for
the week and display the result.
"""


# Initialize an empty sales list.
sales = []

# Initialize a list with the days of the week.
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Loop through the days of the week to get sales for each day.
for day in days:
    daily_sales = float(input("Enter sales for {}: ".format(day)))
    sales.append(daily_sales)

# Calculate the total sales for the week
total_sales = sum(sales)

# Display the result
print(f"The total sales for the week are: ${total_sales}")

"""
Q3 Create a list with at least 5 places you’d like to travel to. Make sure
the list isn’t in alphabetical order
"""

myplaces = ['Ecuador', 'Puerto Rico', 'Paris', 'Miami', 'North Carolina']

# Print the original list
print("Original list: ", myplaces)

# Sort the list in ascending order
myplaces.sort()

# Print the sorted list
print("Sorted List(ascending): ", myplaces)

# Sort the list in descending order
myplaces.sort(reverse=True)

# Print the sorted list in descending order
print("Sorted list (descending): ", myplaces)

"""
#Q4  Write a program that creates a dictionary containing course numbers and the room
numbers of the rooms where the courses meet. The program should also create a
dictionary containing course numbers and the names of the instructors that
teach each course. After that, the program should let the user enter a
course number, then it should display the course’s room number, instructor,
and meeting time.
"""

# Dictionary for Courses
courses_directory = {
    "DATA606": "Statistics and Probability",
    "DATA607": "Data Acquisition and Management",
    "DATA602": "Advanced Programming Techniques",
}

# Dictionary course room numbers
courses_rooms = {
    "DATA606": "Room 1",
    "DATA607": "Room 2",
    "DATA602": "Room 3",
}

# Dictionary for course instructors
courses_instructors = {
    "DATA606": "Prof. Bryer",
    "DATA607": "Prof. Caitlin",
    "DATA602": "Prof. Schettini",
}

# Dictionary for course meeting times
courses_meeting_times = {
    "DATA606": "6:00 PM - 7:00 PM",
    "DATA607": "7:00 PM - 8:00 PM",
    "DATA602": "6:30 PM - 7:30 PM",
}

# Print the course directory
print("Course Directory:", courses_directory)

# Prompt the user to enter a course number
course_number = input("Enter the course number from the course directory ("
                      "case sensitive): ")

# Check if the course number is valid
if course_number in courses_rooms and course_number in courses_instructors and course_number in courses_meeting_times:
    room_number = courses_rooms[course_number]
    instructor = courses_instructors[course_number]
    meeting_time = courses_meeting_times[course_number]
    print("Room number:", room_number)
    print("Instructor:", instructor)
    print("Meeting time:", meeting_time)
else:
    print("Invalid course number. Try again.")

"""
Q5. Write a program that keeps names and email addresses in a dictionary as
key-value pairs. The program should then demonstrate the four options:
● look up a person’s email address,
● add a new name and email address,
● change an existing email address, and
● delete an existing name and email address.
"""

# Initialize an empty dictionary to store name and email address
email_dict = {}

# function to display menu options
def display_menu():
    print("-----------------")
    print("1. Look up email address")
    print("2. Add new name and email address")
    print("3. Change existing email address")
    print("4. Delete name and email address")
    print("5. Show the entire email list")
    print("6. Quit")
    print("-----------------")

# function to look up a person's email address
def lookup_email():
    if len(email_dict) == 0:
        print("The email list is empty.")
    else:
        name = input("Enter the name: ")
        if name in email_dict:
            print("The email address is", email_dict[name])
        else:
            print("The name is not in the email book.")

# function to add a new name and email address
def add_email():
    name = input("Enter the name: ")
    email = input("Enter the email address: ")
    email_dict[name] = email
    print("The email book has been updated.")

# function to change an existing email address
def change_email():
    name = input("Enter the name: ")
    if name in email_dict:
        email = input("Enter the new email address: ")
        email_dict[name] = email
        print("The email address has been updated.")
    else:
        print("The name is not in the email book.")

# function to delete an existing name and email address
def delete_email():
    name = input("Enter the name: ")
    if name in email_dict:
        del email_dict[name]
        print("The name and email address have been deleted.")
    else:
        print("The name is not in the email book.")

# function to show all the names and email addresses
def show_all():
    for name in email_dict:
        print(name, email_dict[name])


# Main program loop
while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        lookup_email()
    elif choice == 2:
        add_email()
    elif choice == 3:
        change_email()
    elif choice == 4:
        delete_email()
    elif choice == 5:
        show_all()
    elif choice == 6:
        break
    else:
        print("Invalid selection. Please try again.")
