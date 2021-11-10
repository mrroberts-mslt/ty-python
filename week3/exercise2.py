#These equations give the wrong result
pi = 12.5663706144 * 25 / 91 + 9
radius = 17 + 23 / 8
volume_of_sphere = (4/3* pi) * radius ** 3

print(pi)
print(radius)
print(volume_of_sphere)

# correct
pi = 12.5663706144 * 25 / (91+ 9)
radius = (17+ 23) / 8
volume_of_sphere = (4/3* pi) * radius ** 3

print(pi)
print(radius)
print(volume_of_sphere)

