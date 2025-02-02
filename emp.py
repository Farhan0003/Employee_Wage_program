import random

def check_attendance():
    print("Welcome to Employee Wages Computation Program")
    # 0: Absent, 1: Full time, 2: Part time
    attendance = random.choice([0, 1, 2])
    return attendance

def emp_daily_wage():
    wage_per_hr = 20
    emp_check = check_attendance()

    if emp_check == 1:
        daily_wage = wage_per_hr * 8
        print(f"Employee is present full day. Daily wage is: {daily_wage}")
    elif emp_check == 2:
        daily_wage = wage_per_hr * 8
        print(f"Employee is present part time. Daily wage is: {daily_wage}")
    else:
        daily_wage = 0
        print(f"Employee is absent. Daily wage is: {daily_wage}")

if __name__ == "__main__":
    emp_daily_wage()




