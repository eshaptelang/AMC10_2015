# This is the thirteenth problem of the 2015 AMC10. For this problem, I started of by recognizing that 5 is a multiple
# of 10, and to have 17 different values of 5, I would need 85 cents. Then, I wrote the two equations 5x + 10y = 85 and
# x + y = 12. I made 2 variables, 85 was assigned to value_needed and 12 was assigned to amount_of_coins. After that, I
# imported numpy, an amazing python package for scientific computing, which works with 2d arrays to help you solve
# simultaneous equations. I made 2 more variables and named them a and b and plugged in specific values that would work
# with numpy to get me my answer. After that, I used np.linalg.solve to actually find our answer and print it. The
# answer that I ended up with is 5.

import numpy as np

amount_of_coins = 12
value_needed = 85
a = [[5, 10], [1, 1]]
b = [value_needed, amount_of_coins]
c = np.linalg.solve(a, b)
print(c)




