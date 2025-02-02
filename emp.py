import random

def check_attendance():
	print("Welcome to Employee wages Computation Program on Master Branch")
	attendance= random.choice([1,0])
	return attendance
def emp_daily_wage():
	wage_per_hr = 20
	emp_check = check_attendance()
	
	if emp_check == 1:
		daily_wage = wage_per_hr * 8
		print(f"the employee is present full day so the daily wage  is : {daily_wage}")
	else:
		daily_wage = 0
		print(f"Employee is absent for the day so the daily wage is : {daily_wage}")

if __name__ == "__main__":
	emp_daily_wage()
