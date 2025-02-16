import random

def check_attendance():
    """Check and return employee attendance status.

    Returns:
        int: 0 if the employee is absent, 1 if full-time, 2 if part-time.
    """
    try:
        return random.choice([0, 1, 2])
    except Exception as e:
        print(f"An error occurred while checking attendance: {e}")
        return 0

def calculate_monthly_wage():
    """Calculate and display the employee's monthly wage based on attendance."""
    wage_per_hr = 20
    total_wage = 0
    total_working_days = 20

    print("Welcome to Employee Wages Computation Program for a Month")

    try:
        for day in range(1, total_working_days + 1):
            emp_check = check_attendance()

            match emp_check:
                case 1:
                    daily_wage = wage_per_hr * 8
                    print(f"Day {day}: Employee is present full day. Daily wage: {daily_wage}")
                case 2:
                    daily_wage = wage_per_hr * 4
                    print(f"Day {day}: Employee is present part time. Daily wage: {daily_wage}")
                case 0:
                    daily_wage = 0
                    print(f"Day {day}: Employee is absent. Daily wage: {daily_wage}")

            total_wage += daily_wage

        print(f"\nTotal wage for the month: {total_wage}")
    except Exception as e:
        print(f"An error occurred while calculating monthly wage: {e}")

def main():
    """Main function to execute the monthly wage computation."""
    calculate_monthly_wage()

if __name__ == "__main__":
    main()
