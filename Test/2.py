# key - function dictionary pairs

def check_age(n):
	if n<=0:
		print("invalid age")
	else:
		print("age processed")

def check_name(s):

	if len(s)==0:
		print("invalid name")
	elif len(s)>15:
		print("entered name is too long to be used")


key_map = {"age" : check_age, "name" : check_name}

key_map["age"](10)