# This is the third problem of the 2015 AMC 10. In this problem, I had to figure out how many additional toothpicks we
# would need to get 5 steps, if 3 steps needed 18 toothpicks. I first found the equation 2 * steps + 2 equalled the
# amount of toothpicks added each time. Then I made a function to be able to find the amount of toothpicks that would
# be needed for any number of steps. I plugged in 5 in the steps, as we needed to find how many toothpicks there would
# be in 5 steps. Then I subtracted how many toothpicks we already have (18).

def toothpick_count(steps):
    result = 0
    for i in range(1, steps + 1):
        result = result + 2 * i + 2
    return result


x = toothpick_count(5)
y = toothpick_count(3)

print(x - y)
