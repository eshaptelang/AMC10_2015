import numpy as np
# This is the eighth problem on the 2015 AMC 10. For this problem, I first made 2 equations, p - 2 = 3(c-2) and p - 4 =
# 4(c - 4). Then I went on to simplify this problem to p - 3 * c = -4 and p - 4 * c = -12. Once I simplified, I imported
# numpy, which is a python package for scientific computing, and made a 2d array to work with numpy. I plugged in the 2
# equations into the numpy linalg solve and it came out with 2 ages. The first age was Pete's current age, which is 20
# and the second age was Claire's, which was 8. After figuring out their current ages, I made a function which will
# determine how many years it will take to get their ages to a certain ratio. The end result, and our answer, was 4.
A = [[1, -3], [1, -4]]
B = [-4, -12]

C = np.linalg.solve(A, B)

pete = C[0]
claire = C[1]

print("Pete's age:" + str(pete))
print("Claire's age:" + str(claire))


def number_of_years(pete, claire, a, b):
    x = (claire * a - pete * b) / (b - a)

    return x


print("Number of years when ratio is 2: 1 is: " + str(number_of_years(pete, claire, 2, 1)))
