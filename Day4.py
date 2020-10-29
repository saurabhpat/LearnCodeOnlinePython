# Question :
# Jack bought a 400 hot dogs for the school picnic.
# If they were contained in packages of 8 hot dogs,
# hot many total packages did he buy?
# Create a python program without using / or % operator

pack_size = 8
hot_dogs = 400
total_packages_bought = 0

while hot_dogs >= pack_size:
    hot_dogs = hot_dogs - pack_size
    total_packages_bought = total_packages_bought + 1

print(total_packages_bought)
