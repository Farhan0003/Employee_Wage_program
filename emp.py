import random

def check_attendance():
    """Check and display employee attendance status.

    This function randomly determines whether an employee is present or absent
    and prints the corresponding status.
    """
    print("Welcome to Employee Wages Computation Program on Master Branch")

    attendance = random.choice([1, 0])

    if attendance == 1:
        print("The employee is present")
    else:
        print("The employee is absent")

if __name__ == "__main__":
    check_attendance()
    print("Welcome to the Employee Wage Computation")
