def arithmetic_arranger(problems, show_answers=False):
    # Check if the number of problems is within the limit
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists to store formatted parts of the problems
    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        # Split the problem into operands and operator
        operand1, operator, operand2 = problem.split()

        # Check if the operator is valid
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        # Check if operands contain only digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if operands have at most four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the maximum length needed for this problem
        max_length = max(len(operand1), len(operand2))

        # Format each part of the problem
        first_line.append(operand1.rjust(max_length + 2))
        second_line.append(f"{operator} {operand2.rjust(max_length)}")
        dash_line.append("-" * (max_length + 2))

        # If show_answers is True, calculate and append the answer
        if show_answers:
            result = str(eval(problem))
            answer_line.append(result.rjust(max_length + 2))

    # Combine the formatted parts into the final result
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dash_line)

    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_line)

    return arranged_problems


# Example usage:
problems1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems1))

problems2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems2, True))
