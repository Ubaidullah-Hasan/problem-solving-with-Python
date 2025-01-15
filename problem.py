#funciton 
'''Write a function add_numbers(a, b) that takes two numbers and returns their sum. If the sum is greater than 100, return "Too Large".'''

def add_numbers(a, b):
    result = a + b
    if(result > 100):
        return "Too Large"
    else:
        return a + b
    
    
print(add_numbers(40, 30))