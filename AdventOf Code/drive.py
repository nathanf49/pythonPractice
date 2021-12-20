def drive(directions):
    depth = 0
    horizontalPosition = 0
    for x in directions:
        direction = x.split()[0]
        length = int(x.split()[1])
        if direction == 'forward':
            horizontalPosition += length
        elif direction == 'backward':
            horizontalPosition -= length
        elif direction == 'down':
            depth += length
        else: # direction is up
            depth -= length
    print(depth * horizontalPosition)

def drive2(directions): # up and down now control aim instead of depth. Depth is controlled by multiplying aim * units moving forward
    depth = 0
    horizontalPosition = 0
    aim = 0
    for x in directions:
        direction = x.split()[0]
        length = int(x.split()[1])
        if direction == 'forward':
            horizontalPosition += length
            depth += aim * length
        elif direction == 'backward':
            horizontalPosition -= length
        elif direction == 'down':
            aim += length
        else: # direction is up
            aim -= length
    print(depth * horizontalPosition)
    print('Horizontal Position: ' + str(horizontalPosition))
    print('Depth: ' + str(depth))

if __name__ == "__main__":
    with open('test_drive.txt') as x:
        directions = x.readlines()
    drive2(directions)