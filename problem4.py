# This is the fourth problem of the 2015 AMC 10. For this problem, I first assigned a number to each person. We basically
# said that Mia has 1x eggs, Sophia has 2x eggs, and Pablo has 6x eggs. But we took away the variable, x, to simplify
# it. Then, I made the equation (Mia + Sophia + Pablo) / 3 to figure out how many eggs each person would have, if it was
# equally separated. I assigned that equation to the variable result. To finally find my answer, I first subtracted Sophia's
# number of eggs by the result, to find how many more eggs she needs. Then I divided it by Pablo's number of eggs to find
# the fraction of Pablo's eggs that he must give. Due to previous knowledge, I knew that the answer was 1/6 in fraction
# form.


mia = 1.0
sophia = 2.0
pablo = 6.0
result = (mia + sophia + pablo) / 3
answer = (result - sophia) / pablo
print(answer)
