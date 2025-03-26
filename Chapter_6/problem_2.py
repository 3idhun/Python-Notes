'''

Q2. WAP to find out whether a student has passed or failed if it requires a total
    of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks
    an input from the user.

'''

'''marks1 = int(input("Enter the marks1 = "))
marks2 = int(input("Enter the marks2 = "))
marks3 = int(input("Enter the marks3 = "))
marks4 = int(input("Enter the marks4 = "))

total_percentage=(100*(marks1+marks2+marks3))/300

if (total_percentage>=40 and marks1>33 and marks2>33 and marks3>33 and marks4>33):
    print("Passed with ",total_percentage)

else:
    print("Failed with ", total_percentage)
'''



mark_list = [int(input("Enter marks: ")) for _ in range(4)]
total_percentage = sum(mark_list) / len(mark_list)                #Here length of marks can be used, because it is stored in a array.

if total_percentage >= 40 and all(marks > 33 for marks in mark_list): #marks is a list, and Python cannot directly compare a list with a number. so we use m. tp access each elements of the list.
    print("Passed with", total_percentage, "%")
else:
    print("Failed with", total_percentage, "%")




