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
                    sum = (sum + value) % 100
                elif direction == "L":
                    sum = (sum - value) % 100
            if print_first_10_lines < 10:
                print_first_10_lines += 1
                print(f"Direction: {direction}, Value: {value}, New Sum: {sum}")
            if sum == 0:
                number_of_times_0 += 1
    print(f"Total: {number_of_times_0}")


if __name__ == "__main__":
    main()