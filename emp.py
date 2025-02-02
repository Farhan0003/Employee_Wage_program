import random

def check_attendance():
    print("Welcome to Employee Wages Computation Program")
    # 0: Absent, 1: Full time, 2: Part time
    attendance = random.choice([0, 1, 2])
    return attendance

def emp_daily_wage():
    wage_per_hr = 20
    emp_check = check_attendance()

    match emp_check:
        case 1:  # Full-time scenario
            daily_wage = wage_per_hr * 8
            print(f"Employee is present full day. Daily wage is: {daily_wage}")
        case 2:  # Part-time scenario
            daily_wage = wage_per_hr * 4
            print(f"Employee is present part time. Daily wage is: {daily_wage}")
        case 0:  # Absent scenario
            daily_wage = 0
            print(f"Employee is absent. Daily wage is: {daily_wage}")

if __name__ == "__main__":
    emp_daily_wage()





