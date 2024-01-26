def palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False  
    
num = int(input())

print("Original Number:", num)
if palindrome(num):
    print("Yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")