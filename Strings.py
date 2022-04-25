# Working with Strings
# phrase = "Giraffe Academy"

print("Giraffe Academy")

print("Giraffe\nAcademy")

print("Giraffe\"Academy")

Phrase = "Giraffe Academy"
print(Phrase)
print(Phrase + " is cool")          # It is called as Concatenation

# Keywords used in Strings
phrase_1 = "giraffe academy"
phrase_2 = "GIRAFFE ACADEMY"
print(phrase_1.upper())             # Convert the characters of string to Uppercase
print(phrase_2.lower())             # Convert the characters of string to Lowercase
print(phrase_1.upper().isupper())   # First capitalize then verify the string

print(len(phrase_1))                # Evaluate the length of String

print(Phrase.index("A"))            # Evaluate the position of the character in a string
print(phrase_1.index("r"))
print(phrase_2.index("Y"))
print(phrase_1[2])                  # To get an individual character of String
print(phrase_1.replace("giraffe",
                       "elephant")) # Replace the old character with new character


