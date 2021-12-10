def get_rows(lines):
    rows = [""]
    for i in range(len(lines[0])):
        for line in lines:
            rows[i] += line[i]
        rows.append("")

    if rows[-1] == "":
        rows.pop()
    return rows

def part1():
    g_rate = ""
    e_rate = ""
    with open("day03.input") as file:
        lines = file.read().split("\n")
        if lines[-1] == "":
            lines.pop()
        for row in get_rows(lines):
            if row.count("1") > row.count("0"):
                g_rate += "1"
                e_rate += "0"
            else:
                g_rate += "0"
                e_rate += "1"
        print(int(g_rate, 2) * int(e_rate, 2))

def part2():
    with open("day03.input") as file:
        lines = file.read().split("\n")
        if lines[-1] == "":
            lines.pop()
        
        curr = 0
        o_lines = lines.copy()
        while len(o_lines) != 1:
            rows = get_rows(o_lines)
            if rows[curr].count("1") >= rows[curr].count("0"):
                o_lines = [line for line in o_lines if line[curr] == "1"]
            else:
                o_lines = [line for line in o_lines if line[curr] == "0"]
            curr += 1

        curr = 0
        c_lines = lines.copy()
        while len(c_lines) != 1:
            rows = get_rows(c_lines)
            if rows[curr].count("1") >= rows[curr].count("0"):
                c_lines = [line for line in c_lines if line[curr] == "0"]
            else:
                c_lines = [line for line in c_lines if line[curr] == "1"]
            curr += 1

        print(int(o_lines[0], 2) * int(c_lines[0], 2))

part1()
part2()
