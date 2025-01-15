def fizzBuzz(n):
    i = 1
    while(i<=n):
        if(i%3 == 0 and i%5 == 0):
            print("FizzBuzz")
        elif(i%5 == 0):
            print("Buzz")
        elif(i%3 == 0):
            print("Fizz")
        else:
            print(i)
        i += 1

if __name__ == '__main__':
    n = int(input().strip())  # ব্যবহারকারীর ইনপুট নেওয়া
    # fizzBuzz(n)  # ফাংশন কল করা
    
# সরাসরি ইনপুট নেওয়া এবং ফাংশন কল
# n = int(input("Enter a number: ").strip())  # ইনপুট নেওয়া
# fizzBuzz(n)  # ফাংশন কল করা
