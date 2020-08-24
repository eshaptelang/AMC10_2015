# This is the second problem of the 2015 AMC 10. In this problem, we had to figure out how many squares and triangles
# there were if we were given 84 sides and 25 shapes. For this problem, we need to import numpy because it is a
# simultaneous equation. Of course there are other ways to solve simultaneous equations, but this is the easiest and
# fastest way. So, first I wrote 2 equations, x + y = 25 and 4x + 3y = 84, in which x equals the number of squares
# and y equals the number of triangles. Then I made a 2d array which has 1x, 1y, 4x, and 3y, which correlate to the
# equations. Then I made a list and put in 25 and 84, which are again, correlating to our equations. After that, I
# used a package from numpy called linalg to solve the problem.

import numpy as np

A = np.array([[1, 1], [4, 3]])
B = np.array([25, 84])
C = np.linalg.solve(A, B)
print(C)
