input_text = input("Enter a sentence or word: ")

new_string = ""

for character in input_text:
    if 65 <= ord(character) <= 90 or 97 <= ord(character) <= 122:
        new_string = new_string + character

new_string = new_string.lower()
if new_string[::-1] == new_string:
    print("That's a palindrome!")
else:
    print("That ain't familyah.")
