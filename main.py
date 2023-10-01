num = int(input("Enter the Number: "))
tempNum = num
reversedNum = 0

# Handle negative numbers
if num < 0:
    print("Negative numbers are not palindromes.")
else:
    while num > 0:
        remainder = num % 10
        reversedNum = reversedNum * 10 + remainder
        num = num // 10

    print("Reversed Number: ", reversedNum)

    if tempNum == reversedNum:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")
