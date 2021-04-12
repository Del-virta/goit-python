points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    if len(coordinates) > 1:
        distance = 0
        i=0
        for point in coordinates[0:len(coordinates)-1]:
            two_points = [point, coordinates[i+1]]
            two_points.sort()
            tuple_points = tuple(two_points)
            distance_one = points.get(tuple_points)
            distance+=distance_one
            i+=1
        return distance
    else:
        return 0
print(calculate_distance([0,1,3,2,0,2]))       