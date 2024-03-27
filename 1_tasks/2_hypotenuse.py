import numpy
# Calculate hypotenuse of a right triangle
leg_1 = 1.6
leg_2 = 2.3
hypotenuse = numpy.hypot(leg_1, leg_2)
print("Hypotenuse:", "{:.3f}".format(hypotenuse))