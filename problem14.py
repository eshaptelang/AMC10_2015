#This is the fourteenth problem on the 2015 AMC 10. In this problem, I started of by importing math ( as seen on line 10)
#After importing math, I made 2 variables, "smaller" which is the radius of our smaller disk, and "larger", which is the
#radius of our larger clock. Then I made an equation to find the length of the arc for just 1 hour on the clock. This
#equation is shown on line 13 and is named "a". But, I found out that I need more than just that to calculate our answer
#So, then I made an equation to calculate the circumference of our smaller disk, as shown on line 14(variable named "b")
#Once doing so, I figured out that to find our answer I must multiply our "a" with 360 and divide by b to find the
# degrees the arrow turns in just 1 hour. As you can see, I did that on line 15 and named the variable "x". After that,
# I found out that we need to add 30 to our "x" because we want to know how many degrees the disk arrow turns in total.
# So I did that on line 16 and named the variable "y". But, we are not finished yet, we now need to divide y by
#360 to be able to find out how much time the disk will need to be able to have it's arrow facing up again. So, in
#conclusion, the answer to this problem is 4o'clock.
import math
smaller = 10
larger = 20
a = (2 * math.pi * larger) / 12
b = 2 * math.pi * smaller
x = (360 * a) / b
y = x + 30
answer = 360 / y
print(answer)
