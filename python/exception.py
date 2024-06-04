a=int(input("First Element"))
b=int(input("Second Element"))
try:  
    div = a/b    
    print(div)  
except ZeroDivisionError:  
    print( "Atepting to divide by zero" )  
finally:  
    print('Demonstrating Exception in Python') 

