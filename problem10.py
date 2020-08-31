# This is the tenth problem of the 2015 AMC 10. First, I imported intertools, which helped us find all the
# permutations of a, b, c, and d. Once we found all of the permutations, we added them to a list called y while also
# bringing all the tuples together. After that, we listed out all of the requirements we needed to solve this problem
# and then we put the results into a list. We were not very interested in what actually was the result, we just wanted
# to know how many results there were, so we took the length of the result and got our answer.

import itertools

x = list(itertools.permutations(["a", "b", "c", "d"]))
y = []
for i in x:
    y.append("".join(i))

result = []
for j in y:
    if "ab" not in j and "ba" not in j and "bc" not in j and "cb" not in j and "cd" not in j and "dc" not in j:
        result.append(j)

print (len(result))
