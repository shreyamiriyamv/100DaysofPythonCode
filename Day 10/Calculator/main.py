import art

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


def calculator():
    print(art.logo)
    num1 = float(input("What is the first number? "))
    should_accumulate = True

    while should_accumulate:

        for symbols in operations:
            print(symbols)

        operation_symbol = input("Pick an operation: ")

        if operation_symbol in operations:
            num2 = float(input("What is the next number? "))


            answer = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or any other letter to exit: ").lower()
            if choice == "y":
                num1 = answer
            elif choice == "n":
                should_accumulate = False
                print("\n" * 20)
                calculator()
            else:
                should_accumulate = False
calculator()



# from art import logo
#
# def calculate():
#     print(logo)
#     first_number = float(input("What's the first number?: "))
#     total = 0
#     is_running = True
#     while is_running:
#         print("+\n-\n*\n/")
#         operation = input("Pick an operation: ")
#         second_number = float(input("What's the next number?: "))
#         if operation == "+":
#             total = add(first_number, second_number)
#         elif operation == "-":
#             total = subtract(first_number, second_number)
#         elif operation == "*":
#             total = multiply(first_number, second_number)
#         elif operation == "/":
#             total = divide(first_number, second_number)
#         else:
#             print("Enter a valid operation")
#             continue
#
#         print(f" {first_number} {operation} {second_number} = {total}")
#         to_continue = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation:").lower()
#         if to_continue == "y":
#             first_number = total
#         else:
#             is_running = False
#             print("\n * 20")
#             calculate()
#
# calculate()