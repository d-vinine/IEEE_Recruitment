import string

# uses two pointer approach
def isPalindrome(text):

    left = 0 # starts at the beginning and moves right
    right = len(text) - 1 # starts at the end and moves left

    while left < right:
        if text[left] != text[right]: # checks if the char at the right and left pointer are different, in which case the word isnt a palindrome
            return False

        left += 1
        right -= 1

    return True


text = input("Enter text: ")

cleanText = "".join(c.lower() for c in text if c not in string.punctuation) # lowercases all letters and removes punctuations
words = cleanText.split() # converts text to a list of words

c = 0
for word in words:
    if isPalindrome(word):
        c += 1

print("Number of palindromes in text:", c)
