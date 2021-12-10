def part1():
    with open("day01.input") as file:
        curr = 0
        prev = 0
        counter = 0
        for line in file.read().split("\n"):
            if not line.isdigit():
                continue
            curr = int(line)
            if curr > prev:
                counter += 1
            prev = curr
        counter -= 1
        return counter

def part2():
    with open("day01.input") as file:
        n1, n2, n3 = -1, -1, -1
        curr = 0
        prev = 0
        counter = 0
        for line in file.read().split("\n"):
            if not line.isdigit():
                continue
            if n1 < 0:
                n1 = int(line)
            elif n2 < 0:
                n2 = int(line)
            elif n3 < 0:
                n3 = int(line)
            else:
                curr = n1 + n2 + n3
                n1, n2, n3 = n2, n3, int(line)
            if curr > prev:
                counter += 1
            prev = curr
        if n1 + n2 + n3 > prev:
            counter += 1
        counter -= 1
        return counter

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
