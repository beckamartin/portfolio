def main():
    print(arithmetic_arranger(["32 + 5 ", "1 - 3801", "15 + 9999", "523 + 49"], True))


def arithmetic_arranger(problems, solve = False):
    if len(problems) > 5:
        return("Error: Too many problems.")

    first = ""
    second = ""
    lines = ""
    resx = ""
    arranged_problems = []

    for problem in problems:
        first_num, operator, second_num = problem.split()

        if operator not in "+-":
            return("Error: Operator must be '+' or '-'.")
        elif not first_num[0].isdigit() or not second_num.isdigit():
            return("Error: Numbers must only contain digits.")
        elif len(str(first_num)) > 4 or len(str(second_num)) > 4:
            return("Error: Numbers cannot be more than four digits.")

        sum = int()

        if operator == "+":
            sum = int(first_num) + int(second_num)
        elif operator == "-":
            sum = int(first_num) - int(second_num)

        max_len = max(len(first_num), len(second_num)) + 2
        top = str(first_num).rjust(max_len)
        bottom = operator + str(second_num).rjust(max_len - 1)
        line = ""
        res = str(sum).rjust(max_len)

        for _ in range(max_len):
            line += "-"
        
        if problem != problems[-1]:
            first += top + "    "
            second += bottom + "    "
            lines += line + "    "
            resx += res + "    "
        else:
            first += top
            second += bottom
            lines += line
            resx += res

    if solve:
        arranged_problems = first + "\n" + second + "\n" + lines + "\n" + resx
    else:
        arranged_problems = first + "\n" + second + "\n" + lines

    return arranged_problems

if __name__ == "__main__":
    main()