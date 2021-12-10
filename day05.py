# I'm not cool for 1D arrays :(

# grid = [[x1, x2, ...], ...]
# vents = [[x1, y1, x2, y2], ...]
def get_data(can_diagonal=False):
    grid_size = [0, 0]
    grid = []
    vents = []
    with open("day05.input") as file:
        lines = file.read().split("\n")
        if lines[-1] == "":
            lines.pop()

        # Get the vents and find the size of the grid.
        for line in lines:
            positions = line.split("->")
            is_start = True
            for position in positions:
                numbers = position.split(",")
                x = int(numbers[0])
                y = int(numbers[1])
                if is_start:
                    vents.append([])
                is_start = not is_start

                vents[-1].append(x)
                vents[-1].append(y)
                if x > grid_size[0]:
                    grid_size[0] = x
                if y > grid_size[1]:
                    grid_size[1] = y

        # Make the grid.
        for y in range(grid_size[1] + 1):
            grid.append([])
            for x in range(grid_size[0] + 1):
                grid[-1].append(0)
        for vent in vents:
            x1, y1 = vent[0], vent[1]
            x2, y2 = vent[2], vent[3]
            if y1 == y2:
                if x1 < x2:
                    for i in range(x2 - x1 + 1):
                        grid[y1][x1 + i] += 1
                else:
                    for i in range(x1 - x2 + 1):
                        grid[y1][x1 - i] += 1
            elif x1 == x2:
                if y1 < y2:
                    for i in range(y2 - y1 + 1):
                        grid[y1 + i][x1] += 1
                else:
                    for i in range(y1 - y2 + 1):
                        grid[y1 - i][x1] += 1
            elif can_diagonal:
                distance = [abs(x1 - x2), abs(y1 - y2)]
                if distance[0] != distance[1]:
                    continue
                # Yeah, I'm doing this.
                x_sign = 1
                y_sign = 1
                if x1 > x2:
                    x_sign = -1
                if y1 > y2:
                    y_sign = -1
                for i in range(distance[0] + 1):
                    grid[y1 + i * y_sign][x1 + i * x_sign] += 1
        return grid, grid_size, vents

def print_grid(grid):
    for line in grid:
        for x in line:
            print(x, end=" ")
        print()    

def part1():
    grid, grid_size, vents = get_data()
    two_count = 0
    for line in grid:
        for x in line:
            if x > 1:
                two_count += 1
    print(two_count)

def part2():
    grid, grid_size, vents = get_data(can_diagonal=True)
    two_count = 0
    for line in grid:
        for x in line:
            if x > 1:
                two_count += 1
    print(two_count)

part1()
part2()
