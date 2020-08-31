# This is the ninth problem of the 2015 AMC 10. First, I solved the problem without using python by doing simple
# arithmetic. From that, got an equation which I could use for any percentage input which is the value of ratio in this
# program. Then, I printed out the answer but I had to make sure that it was in percentage form, so I multiplied it by
# 100 and subtracted by 1.
percentage = 10.0
ratio = (percentage/100 + 1) ** 2
print(ratio * 100 -1)

