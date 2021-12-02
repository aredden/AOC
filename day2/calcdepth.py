lines = [i.strip() for i in open("input.txt", "r").readlines()]
depth = 0
horizontal = 0
aim = 0

def move(direction, amount):
    global depth, horizontal, aim
    if direction == "down":
        aim += int(amount)
    elif direction == "up":
        aim -= int(amount)
    elif direction == "forward":
        horizontal += int(amount)
        depth += aim * int(amount)
    else:
        raise Exception("Unknown direction: " + direction + " with amount " + amount)

for l in lines:
    move(*l.split())
    
print(depth, horizontal)
print(depth*horizontal)