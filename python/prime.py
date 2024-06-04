def prime(n):
        if n<=1:
            return 0
        if n==2:
            return 1
        else:
            for i in range(2,n):
                if(n%i)==0:
                    return 0
                return 1
x=int(input("enter a integer number "))
y=prime(x)
if y==1:
    print("given number is prime number")
else:
    print("given number is not a prime number")
