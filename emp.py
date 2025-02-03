import random

def check_attendance():
    # 0: Absent, 1: Full time, 2: Part time
    return random.choice([0, 1, 2])

def calculate_wages():
    wage_per_hr = 20
    total_wage = 0
    total_working_days = 0
    total_working_hours = 0
    max_working_hours = 100
    max_working_days = 20

    print("Welcome to Employee Wages Computation Program with Condition")

    while total_working_days < max_working_days and total_working_hours < max_working_hours:
        emp_check = check_attendance()

        match emp_check:
            case 1:  # Full-time scenario
                daily_hours = 8
                print(f"Day {total_working_days + 1}: Employee is present full day. Worked hours: {daily_hours}")
            case 2:  # Part-time scenario
                daily_hours = 4
                print(f"Day {total_working_days + 1}: Employee is present part time. Worked hours: {daily_hours}")
            case 0:  # Absent scenario
                daily_hours = 0
                print(f"Day {total_working_days + 1}: Employee is absent. Worked hours: {daily_hours}")

        # Update total hours, days, and wages
        total_working_hours += daily_hours
        total_working_days += 1
        daily_wage = daily_hours * wage_per_hr
        total_wage += daily_wage

    print("\n--- Monthly Wage Summary ---")
    print(f"Total Working Days: {total_working_days}")
    print(f"Total Working Hours: {total_working_hours}")
    print(f"Total Wage: {total_wage}")

if __name__ == "__main__":
    calculate_wages()







