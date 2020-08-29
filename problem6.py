# This is the sixth problem in the 2015 AMC 10. To solve this problem, I first figured out how to solve the equation
# without using python. After solving, I found an equation that would work for any number of "times". Times being how
# many times the sum is bigger than the difference. The equation that I got was a/b = (x + 1)/(x-1), with x being our
# time. With this information, I set times to 5 for this problem ( this can be changed and it will still work) and used
# the equation that I got to figure out the fraction.

times = 5

numerator = times + 1
denominator = times - 1

print(str(numerator) + "/" + str(denominator))