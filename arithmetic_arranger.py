def arithmetic_arranger(problems, display_result=False):
    operators = ['+', '-']
    problems_limit = 5
    numbers_len_limit = 4

    """ VERIFY USER INPUTS """

    # Check if there are more problems than the limit allowed
    if (len(problems) > problems_limit):
        return "Error: Too many problems."

    # Check if all problems have valid operators
    for problem in problems:
        if (problem.split()[1] not in operators):
            return "Error: Operator must be '+' or '-'."

    # Check if all problems have valid numbers
    for problem in problems:
        if (not problem.split()[0].isdigit() or not problem.split()[2].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check if all problems have numbers less than five digits
    for problem in problems:
        if (len(problem.split()[0]) > numbers_len_limit or len(problem.split()[2]) > numbers_len_limit):
            return "Error: Numbers cannot be more than four digits."

    """ SOLVE PROBLEMS """

    # first number
    first_row = ""
    # operator and number
    second_row = ""
    # dashes
    third_row = ""
    # solution
    fourth_row = ""

    # First Row
    for problem in problems:
        math_problem = problem.split()
        operator = math_problem[1]
        number_1 = math_problem[0]
        number_2 = math_problem[2]
        longest_number = max(len(number_1), len(number_2))

        # check if it's the last problem
        is_last_problem = True if (problems.index(
            problem) == len(problems) - 1) else False

        # * Update first row
        first_row += number_1.rjust(longest_number + 2)
        first_row += " " * 4 if not (is_last_problem) else "\n"

        # * Update second row
        second_row += operator
        second_row += number_2.rjust(longest_number + 1)
        second_row += " " * 4 if not (is_last_problem) else "\n"

        # * Update third row (dashes)
        third_row += "-" * (longest_number + 2)

        if not (is_last_problem):
            third_row += " " * 4
        elif display_result:
            third_row += "\n"

        # * Update fourth row (solutions)
        # Check if the user wants the solutions
        if (display_result):
            # Calculate solution
            math_result = str(int(number_1) + int(number_2)) if (
                operator == "+") else str(int(number_1) - int(number_2))

            fourth_row += math_result.rjust(longest_number + 2)
            if not (is_last_problem):
                fourth_row += " " * 4

    result = first_row + second_row + third_row

    # Return the results
    if (display_result):
        result += fourth_row

    return result
