import numpy
# Change to degrees
# 1. a)
degs_a1 = numpy.rad2deg(2.493)
# 1. b)
degs_b1 = numpy.rad2deg(0.911)
print("{:.3f}".format(degs_a1), "{:.3f}".format(degs_b1))
print("-" * 15)
# Change to radians
# 2. a)
radians_a2 = numpy.deg2rad(137.7)
# 2. b)
radians_b2 = numpy.deg2rad(62.3)
print("{:.3f}".format(radians_a2), "{:.3f}".format(radians_b2))
# Array of radians
radians_list = numpy.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
print("-" * 15)
for deg in radians_list:
    print(f"| {deg}{" " if deg < 100 else ""} | {"{:.3f}".format(numpy.radians(deg))} |")
print("-" * 15)

# Calculate hypotenuse of a right triangle
leg_1 = 1.6
leg_2 = 2.3
hypotenuse = numpy.hypot(leg_1, leg_2)
print("Hypotenuse:", "{:.3f}".format(hypotenuse))
