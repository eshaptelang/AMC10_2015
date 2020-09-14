# This is the eleventh problem of the 2015 AMC 10. For this problem, I started of by making 2 variables, length and
# width, which represent the length  and width of our rectangle. ( Imagine that we have an x next to these)We also have
# to find the diagonal of the rectangle,so we use the pythagorean theorem to find the length of d. I decided not to
# square root d because we need diagonal squared for our equation, but we should remember that diagonal = 5. From this,
# I found out that x (the imaginary x next to our length and width) would equal d/5. Now, we can put all the pieces
# together. Remember that our area is 4 * 3 which equals 12x, and we know x = d/5. So, 12 * d/5 would equal 12d to the
# power 2 over 25. ( We made it d squared because our question asks for our answer in that form). Now we would take out
# the d ^ 2, getting our answer of 12/25.
length = 4.0
width = 3.0
d = (length ** 2) + (width ** 2)
x = d/5
a = length * width
print(a / 25)
print(str(a) + "/" + str(25))