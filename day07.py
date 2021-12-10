def part1():
    with open("day07.input") as file:
        pos_list = [int(c) for c in file.readlines()[0].split(",")]
        pos_set = set(pos_list)

        min_fuel_cost = 999999
        for spos in pos_set:
            fuel_cost = 0
            for lpos in pos_list:
                fuel_cost += abs(lpos - spos)
            if fuel_cost < min_fuel_cost:
                min_fuel_cost = fuel_cost
        print(min_fuel_cost)

def part2():
    with open("day07.input") as file:
        pos_list = [int(c) for c in file.readlines()[0].split(",")]
        pos_set = set(pos_list)
        # The number does not need to be in the list :(

        smallest_pos = 999999
        biggest_pos = 0
        for spos in pos_set:
            if spos < smallest_pos:
                smallest_pos = spos
            elif spos > biggest_pos:
                biggest_pos = spos

        min_fuel_cost = 999999999999
        for pos in range(smallest_pos, biggest_pos + 1):
            fuel_cost = 0
            for lpos in pos_list:
                for i in range(abs(lpos - pos) + 1):
                    fuel_cost += i
            if fuel_cost < min_fuel_cost:
                min_fuel_cost = fuel_cost
        print(min_fuel_cost)

part1()
part2()
