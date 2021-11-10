#These equations give the wrong result
pi = 12.5663706144 * 25 / 91 + 9
radius = 17 + 23 / 8
volume_of_sphere = (4/3* pi) * radius ** 3

expected_pi = 3.14159265359
expected_radius = 5
expected_volume = 523.5987755983333

print("pi: ",pi)
print("radius: ",radius)
print("volume: ",volume_of_sphere)

# corrected
pi = 12.5663706144 * 25 / (91+ 9)
radius = (17 + 23) / 8
volume_of_sphere = (4/3* pi) * radius ** 3

print(pi)
print(radius)
print(volume_of_sphere)

