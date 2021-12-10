n = 9

def create_days(fishes):
    # [fish count on day 0, ..., fish count on day 8]
    days = [0] * n
    for fish in fishes:
        days[fish] += 1
    return days

def update_days(days):
    day0 = days[0]
    # Move everything to the left.
    for i in range(n):
        if i != 0:
            days[i - 1] = days[i]
    days[-1] = 0
    # Add new fish and reset the old ones.
    days[-1] += day0
    days[6] += day0

def get_fish_count(days):
    count = 0
    for day in days:
        count += day
    return count

def part1():
    with open("day06.input") as file:
        fishes = [int(fish) for fish in file.readlines()[0].split(",")]
        days = create_days(fishes)
        for _ in range(80):
            update_days(days)
        print(get_fish_count(days))        

def part2():
    with open("day06.input") as file:
        fishes = [int(fish) for fish in file.readlines()[0].split(",")]
        days = create_days(fishes)
        for _ in range(256):
            update_days(days)
        print(get_fish_count(days))     

part1()
part2()
