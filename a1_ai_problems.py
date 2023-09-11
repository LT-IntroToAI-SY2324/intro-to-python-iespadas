# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

for num in range(1, 15):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#seperation 
def is_palindrome(input_str):
    clean_str = ''.join(input_str.split()).lower()
    
    return clean_str == clean_str[::-1]

print(is_palindrome("racecar"))  # Should return True
print(is_palindrome("Hello, World!"))  # Should return False
#problem 3
sum_of_digits(12345)  # Should return 15

#problem 4
is_prime(17)  # Should return True
is_prime(4)   # Should return False
# problem 5
fibonacci(7)  # Should return [0, 1, 1, 2, 3, 5, 8]

# problem 6
reverse_string("Hello, World!")  # Should return "!dlroW ,olleH"



