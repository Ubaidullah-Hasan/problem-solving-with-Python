#funciton 
'''Write a function add_numbers(a, b) that takes two numbers and returns their sum. If the sum is greater than 100, return "Too Large".'''

def add_numbers(a, b):
    result = a + b
    if(result > 100):
        return "Too Large"
    else:
        return a + b
    
    
# print(add_numbers(40, 30))


"""For Loop Problem
Problem: Print all even numbers between 1 and 50 using a for loop.
Sample Output:
Output: 2, 4, 6, 8, ..., 50"""

for x in range(2, 51, 2):
    # print(x)
    pass
    
    
'''While Loop Problem
Problem: Calculate the factorial of a given number using a while loop.
Sample Input/Output:
Input: 5
Output: 120
(Explanation:5×4×3×2×1=120)'''

num = 6
result = 1
while(num > 0):
    result = result * num
    num = num - 1
    
print(result)