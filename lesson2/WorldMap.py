"from random import randint

# | | | | | |
# | | | | | |
# | | | | | |
# | | | | | |
# | | | | | |

n = int(input('Map size n: '))
m = int(input('Map size m: '))

x = int(input('Player x: '))
y = int(input('Player y: '))

portal_x = randint(0, n - 1)
portal_y = randint(0, m - 1)

print(f'Generating map {n}x{m}...')
direction = 'initially'

while True:
    
    world_map = ''

    for i in range(m):

        row = ''

        for j in range(n):

            cell = '| '

            if x == j and y == i:
                print(f'Moving character {direction} to {x}:{y}')
                cell = '|X'
            elif portal_x == j and portal_y == i:
                cell = '|O'
                
            row += cell

        row += '|\n'

        world_map += row

    print(world_map)

    if x == portal_x and y == portal_y:
        print('You won!')
        break

    action = input('Action: ')

    if action == 'move':
        
        direction = input('Direction: ')

        if direction == 'up' and y > 0:
            y -= 1
        elif direction == 'down' and y < m - 1:
            y += 1
        elif direction == 'left':
            x -= 1
            x = n - 1 if x < 0 else x
        elif direction == 'right':
            x += 1
            x = 0 if x == n else x
        else:
            print('Wrong direction. Please try again.')

    elif action == 'exit':
        break
    else:
        print('Wrong action. Please try again.')

print('Game Over')
"