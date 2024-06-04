import re
Div="BCA 4 B"

print(re.fullmatch("BCA 4 A",Div))
print(re.fullmatch("BCA 4 B",Div))
print(re.search("BCA",Div))
print(re.findall("A",Div))
print(re.sub("B","A",Div))
print(re.findall("\d",Div))
