import re
input_file = "input.txt"


def main():
    sum = 50
    number_of_times_0 = 0
    print_first_10_lines = 0 
    with open(input_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            match = re.match(r"([LR])(\d+)", line)
            if match:
                direction = match.group(1)
                value = int(match.group(2))
                if direction == "R":
                    for x in range(value): 
                        sum = (sum + 1) % 100
                        if sum == 0:
                            number_of_times_0 += 1
                elif direction == "L":
                    for x in range(value): 
                        sum = (sum - 1) % 100
                        if sum == 0:
                            number_of_times_0 += 1
            if print_first_10_lines < 10:
                print_first_10_lines += 1
                print(f"Direction: {direction}, Value: {value}, New Sum: {sum}")
    print(f"Total: {number_of_times_0}")


if __name__ == "__main__":
    main()


