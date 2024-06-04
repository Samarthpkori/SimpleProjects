import math   

def Roots(a, b, c): 
    dis = b * b - 4 * a * c    #Discriminant 
    sqrt1 = math.sqrt(abs(dis))  
    
    if dis > 0:  
        print(" real and different roots ")  #1,2,1
        print((-b + sqrt1) / (2 * a))  
        print((-b - sqrt1) / (2 * a))

    elif dis == 0:  
        print(" real and same roots")   #1,10,24
        print(-b / (2 * a))  
    else:  
        print("Complex Roots")  # 10,20,30
        print(- b / (2 * a), " + i", sqrt1)  
        print(- b / (2 * a), " - i", sqrt1) 

a = int(input('Enter a:'))  
b = int(input('Enter b:'))  
c = int(input('Enter c:'))  

if a == 0:  
    print("Input correct quadratic equation")  

else:  
    Roots(a, b, c) 
