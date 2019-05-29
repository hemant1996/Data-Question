def multiply(a,b):
    total = 0
    counter = 0
    while counter < b:
        total += a
        counter += 1
    return total

def getFact(n):
   if n == 1:  
       return n  
   else:  
       return n*getFact(n-1)
number = int(input())
number2 = int(input())
multiplication_value = multiply(number, number2)
if(number > number2):
    factorial_value = getFact(number)
else:
    factorial_value = getFact(number2)
result = multiply(factorial_value, multiplication_value)
print("multiplication_value",multiplication_value)
print("factorial_value",factorial_value)
print("result",result)