# if else 
if 5<10 :
    print("condition is true")
    
# recursion
def factorial_result(num):
    if(num>0):
        print(num)
        result = num + factorial_result(num - 1)
    else:
        result = 0
    return result

print("Recursion Example Results:")
print(factorial_result(4))