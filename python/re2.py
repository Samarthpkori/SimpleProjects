import re
p=re.compile(r"[A-Za-z\s]+")
r=re.compile(r"[0-9]+")

name=input("enter the string:")
rno=input("enter register no:")

print("----------------")
print("computer science department,dharwad")
print("student attendence information")
print("------------------")

if re.fullmatch(p,name):
    print(f"student name is{name}\n")
else:
    print("enter student name correctly")

if re.fullmatch(r,rno):
    print(f"student regno is{rno}\n")
    print(f"{name} attends the classes regularly")
else:
    print("rno should be number")