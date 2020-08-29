# This is the seventh problem on the 2015 AMC 10. To solve this problem, I first made 2 variables, x which will print
# all of the numbers in the list, and y which will print the number of items that were printed at the end. Then I made a
# while loop and placed the limit to 73 and said that the x should go by 3s and the y should go up 1 each time. Then I
# printed y and got my answer of 21.

x = 13
y = 0
while x <= 73:
    x = x + 3
    y = y + 1
print(y)
