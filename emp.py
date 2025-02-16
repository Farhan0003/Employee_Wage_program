import random

def check_attendance():
    """Check and return employee attendance status.

    Returns:
        int: 0 if the employee is absent, 1 if full-time, 2 if part-time.
    """
    print("Welcome to Employee Wages Computation Program")

    try:
        return random.choice([0, 1, 2])
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
            print(f"Employee is present full day. Daily wage is: {daily_wage}")
        elif emp_check == 2:
            daily_wage = wage_per_hr * 4
            print(f"Employee is present part time. Daily wage is: {daily_wage}")
        else:
            daily_wage = 0
            print(f"Employee is absent. Daily wage is: {daily_wage}")
    except Exception as e:
        print(f"An error occurred while calculating daily wage: {e}")

def main():
    """Main function to execute the employee wage computation."""
    emp_daily_wage()

if __name__ == "__main__":
    main()




