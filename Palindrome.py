word1 = input("Enter a Word/Number : ")

def reverse(result):
    return result[::-1]
if (reverse(word1) == word1):
    print("Its Palindrome")
else:
    print("Its not Palindrome")
