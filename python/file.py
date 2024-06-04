f=open("s.txt",mode='w')
f.write('Ambika')
f.close
print('yes it is done')

f=open('s.txt',mode='r')
data=f.read()
print("-----------")
print(data)
f.close
