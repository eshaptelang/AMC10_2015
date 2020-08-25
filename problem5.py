# This is the fifth problem in the 2015 AMC 10. To solve this problem, I first assigned 4 variables, a variable with the
# average including payton, one with the total amount of students, a variable with the average not including payton,
# and the amount of students without Payton. With these variables I created 2 equations, one calculating how many points
# the class earned without Payton, and one calculating how many points the class earned with Payton. Then I subtracted
# the points without Payton from the points with Payton, getting our answer of 95.
total_students = 15
students_without_payton = 14
average = 81
average_without_payton = 80
sum_without_payton = students_without_payton * average_without_payton
sum_with_payton = total_students * average
answer = sum_with_payton - sum_without_payton
print(answer)
