import random

def check_attendance():
	print("Welcome to Employee  wages Computation Program  on Master  Branch")
	attendance=random.choice([1,0])
	if attendance == 1:
		print("The  employee is present")
	else:
		print("The employee is absent")

if  __name__=="__main__":
	check_attendance()
	print("welcome to the employee wage Computation")
