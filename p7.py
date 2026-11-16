text = input("enter your string:")

reversed_text = text[::-1]
print(reversed_text)

# checking palindrome or not!

text = input("Enter a word to check palindrome:")

force_the_text = text.lower()

if force_the_text == force_the_text[::-1]:
    print("This is a palindrome number")
else:
    print("This is not a palindrom number")
