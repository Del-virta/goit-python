points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    distance = 0
    if len(coordinates) <=1:
        return 0
    else:
        for i in range(len(coordinates)-1):
            couple = (coordinates[i],coordinates[i+1])
            coordinate = sorted(couple)
            for key in points.keys():
                if tuple(coordinate) == key:
                    distance+=points.get(key)
        return distance 
print(calculate_distance([0,1,3,2,0,2])) 