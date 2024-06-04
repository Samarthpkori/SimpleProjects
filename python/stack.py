l=[]
while True:
    c=int(input
                ('''
                        1.push element
                        2.pop element
                        3.peek element
                        4.display element
                        5.exit
                        enter the choice
                ''')
            )

    if c==1:
        n=input("enter the element\n")
        l.append(n)
        print(l)

    elif c==2:
        if len(l)==0:
            print("empty stack")
        else:
            p=l.pop()
            print(p)
            print(l)

    elif c==3:
        if len(l)==0:
            print("empty stack")
        else:
            print("last stack value\n",l[-1])

    elif c==4:
        print("display stack\n",l)

    elif c==5:
        break
