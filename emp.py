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

def calculate_wages():
    """Calculate and display the employee's wages based on working hours and days with conditions."""
    WAGE_PER_HR = 20
    TOTAL_WAGE = 0
    TOTAL_WORKING_DAYS = 0
    TOTAL_WORKING_HOURS = 0
    MAX_WORKING_HOURS = 100
    MAX_WORKING_DAYS = 20

    print("Welcome to Employee Wages Computation Program with Condition")

    try:
        while TOTAL_WORKING_DAYS < MAX_WORKING_DAYS and TOTAL_WORKING_HOURS < MAX_WORKING_HOURS:
            emp_check = check_attendance()

            match emp_check:
                case 1:
                    daily_hours = 8
                    print(f"Day {TOTAL_WORKING_DAYS + 1}: Employee is present full day. Worked hours: {daily_hours}")
                case 2:
                    daily_hours = 4
                    print(f"Day {TOTAL_WORKING_DAYS + 1}: Employee is present part time. Worked hours: {daily_hours}")
                case 0:
                    daily_hours = 0
                    print(f"Day {TOTAL_WORKING_DAYS + 1}: Employee is absent. Worked hours: {daily_hours}")

            TOTAL_WORKING_HOURS += daily_hours
            TOTAL_WORKING_DAYS += 1
            daily_wage = daily_hours * WAGE_PER_HR
            TOTAL_WAGE += daily_wage

        print("\n--- Monthly Wage Summary ---")
        print(f"Total Working Days: {TOTAL_WORKING_DAYS}")
        print(f"Total Working Hours: {TOTAL_WORKING_HOURS}")
        print(f"Total Wage: {TOTAL_WAGE}")
    except Exception as e:
        print(f"An error occurred while calculating wages: {e}")

def main():
    """Main function to execute the wage computation."""
    calculate_wages()

if __name__ == "__main__":
    main()
