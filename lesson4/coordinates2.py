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
    coordinate = []
    if len(coordinates) <=1:
        return 0
    else:
        for idx, value in enumerate(coordinates[0:len(coordinates)-1]):
            couple = [coordinates[idx],coordinates[idx+1]]
            couple.sort()
            coordinate = tuple(couple)
            distance+=points.get(coordinate)
        return distance 
print(calculate_distance([0,1,3,2,0,2]))        
