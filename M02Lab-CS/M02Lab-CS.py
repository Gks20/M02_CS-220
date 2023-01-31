# Author Gregory K. Shaw
# File name M02Lab-CS
# The purpose of this application is to determine whether a student has
# made the Dean's List and Honor Roll based off the students GPA.


# input of the students last name
lastName = input("Please enter your last name :")

# end processing if last name contains 'ZZZ'
if ("ZZZ") in lastName:
    print("Goodbye.")
    raise SystemExit

# input of students first name
firstName = input("Please enter your first name :")

# set variables for Dean's List, Honor Roll, and GPA.
dean = 3.5
honor = 3.25
gpa = float(input("Please enter your GPA :"))

if gpa > dean:
    print("You have made the Dean's list!")

elif gpa < dean:
    print("You have not made the Dean's list.")

if gpa > honor:
    print("You have made Honor Roll!")

elif gpa < honor:
    print("You have not made Honor Roll.")
