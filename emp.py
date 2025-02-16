import random

def check_attendance():
    """Check and return employee attendance status.

    Returns:
        int: 1 if the employee is present, 0 if absent.
    """
    print("Welcome to Employee Wages Computation Program on Master Branch")

    try:
        return random.choice([1, 0])
    except Exception as e:
        print(f"An error occurred while checking attendance: {e}")
        return 0

def emp_daily_wage():
    """Calculate and display the employee's daily wage based on attendance."""
    wage_per_hr = 20

    try:
        emp_check = check_attendance()

        if emp_check == 1:
            daily_wage = wage_per_hr * 8
            print(f"The employee is present full day, so the daily wage is: {daily_wage}")
        else:
            daily_wage = 0
            print(f"The employee is absent for the day, so the daily wage is: {daily_wage}")
    except Exception as e:
        print(f"An error occurred while calculating daily wage: {e}")

def main():
    """Main function to execute the employee wage computation."""
    emp_daily_wage()

if __name__ == "__main__":
    main()




