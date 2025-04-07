job = input("Are you an administrator, teacher, or student?: ")
if job == "administrator" or job == "teacher":
    print("Administrators and teachers get keys!")
elif job == "student":
    print("Students do not get keys!")
else:
    print("You can only be an administrator, teacher, or student!")