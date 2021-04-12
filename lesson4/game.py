def game(terra, power):
    for power_list in terra:
        for power_plus in power_list:
            if power >= power_plus:
                power+=power_plus
            else:
                break
    return power
print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))