def part1():
    h_pos = 0
    depth = 0
    with open("day02.input") as file:
        for line in file:
            data = line.split(" ")
            if len(data) < 2:
                continue
            if data[0] == "forward":
                h_pos += int(data[1])
            elif data[0] == "down":
                depth += int(data[1])
            elif data[0] == "up":
                depth -= int(data[1])
        print(h_pos * depth)

def part2():
    h_pos = 0
    depth = 0
    aim = 0
    with open("day02.input") as file:
        for line in file:
            data = line.split(" ")
            if len(data) < 2:
                continue
            if data[0] == "forward":
                units = int(data[1])
                h_pos += units
                depth += aim * units
            elif data[0] == "down":
                aim += int(data[1])
            elif data[0] == "up":
                aim -= int(data[1])
        print(h_pos * depth)

part1()
part2()
