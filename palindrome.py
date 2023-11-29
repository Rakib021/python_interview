def isPalindrome(word):
    return word == word[::-1]

word ="mamo"
if isPalindrome(word):
    print("Yes")
else:
    print("no")