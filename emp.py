import random

def check_attendance():
    # 0: Absent, 1: Full time, 2: Part time
    return random.choice([0, 1, 2])

def calculate_monthly_wage():
    wage_per_hr = 20
    total_wage = 0
    total_working_days = 20

    print("Welcome to Employee Wages Computation Program for a Month")

    for day in range(1, total_working_days + 1):
        emp_check = check_attendance()

        match emp_check:
            case 1:  # Full-time scenario
                daily_wage = wage_per_hr * 8
                print(f"Day {day}: Employee is present full day. Daily wage: {daily_wage}")
            case 2:  # Part-time scenario
                daily_wage = wage_per_hr * 4
                print(f"Day {day}: Employee is present part time. Daily wage: {daily_wage}")
            case 0:  # Absent scenario
                daily_wage = 0
                print(f"Day {day}: Employee is absent. Daily wage: {daily_wage}")
        
        # Accumulate the daily wage
        total_wage += daily_wage

    print(f"\nTotal wage for the month: {total_wage}")

if __name__ == "__main__":
    calculate_monthly_wage()






