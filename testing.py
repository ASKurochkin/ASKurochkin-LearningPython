import random

def asteroid_position(rings_number: int, asteroid_number: int):
    asteroid_distance = []
    asteroid_angle = []
    asteroid_position = {}
    for distance in range(rings_number):
        asteroid_distance.append(random.randrange(160, 210, 10))
    counter = 0
    while counter <= len(asteroid_distance) - 1:
        for angle in range(asteroid_number):
            asteroid_angle.append(random.randrange(0, 360))
        asteroid_position[asteroid_distance[counter]] = asteroid_angle
        counter += 1
        asteroid_angle = []
    return asteroid_position

print(asteroid_position(4, 10))
