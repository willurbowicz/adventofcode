import re


def get_digit(x):
    letter_digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return x if x.isnumeric() else str(letter_digits.index(x))


def main():

    calibration_sum = 0
    for x in open("input.txt"):
        digits = re.findall(r"\d", x)
        calibration_sum += int(digits[0] + (digits[-1]))
    print("Part 1 solution: " + str(calibration_sum))

    calibration_sum = 0
    for z in open("input.txt"):
        digits = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", z)
        calibration_sum += int(get_digit(digits[0]) + get_digit(digits[-1]))
    print("Part 2 solution: " + str(calibration_sum))


if __name__ == "__main__":
    main()
