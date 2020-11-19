def nearest_palindrome(number):
    while True:
        rev = 0
        temp = number
        while (temp > 0):
            digit = temp % 10
            temp = temp // 10
            rev = rev * 10 + digit
        print(rev)
        if (rev == number):
            break
        else:
            number += 1
    return rev


number = 9
print("The Nearesr Palindrome is:",nearest_palindrome(number+1))