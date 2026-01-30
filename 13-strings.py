""" STRINGS """
# A String is a sequence of characters written inside quotes.
# It can include letters, numbers, symbols and spaces.
"""
• Python does not have a separate character type.
• A single character is treated as a string of length one.
• Strings are commonly used for text handling and manipulation.
"""

str1 = "This is a string."
str2 = 'strings'
str3 = """This is also a string.""" # Used for multi-line string

handling = "Aman's Bike."

print(handling)


""" Basic Operations """
# 1. Concatenation (Joining Strings)
#   Use + to join strings

a = "Hello"
b = "World"
print(a + " " + b)

# 2. Repetition (Repeating a String)
#   Use * to repeat a string.

print("Hi " * 3)

# 3. Indexing (Accessing Characters)
#   Each character has a position (index).
#   Index starts from 0.
#   Can't change/modify charecter using indexing

text = "Python"
print(text[0])
print(text[3])

# 4. Slicing (Getting Part of a String)
#   Used to get a part of a string.
#   It have special feature of backward indexing / negative indexing.

text = "Python"
print(text[0:3]) # Start from 0 and ends at 2 (end-1). If there is no ending index or starting index it assumes that from starting ot till ending.

# 5. Length of a String
#   Use len() to find string length.

text = "Python"
print(len(text))
text_2 = "  "
print(len(text_2))

# 6. Checking a String (Membership)
#   Use in to check if something exists.

print("Py" in "Python")


"""String Functions"""

text = "  Hello Python  "

# 1. upper() – Convert to Uppercase

print(text.upper())

# 2. lower() – Convert to Lowercase

print(text.lower())

# 3. strip() – Remove Extra Spaces

print(text.strip())

# 4. replace() – Replace Text

print(text.replace("Python", "World")) # First give old value then new value

# 5. find() – Find Position of a Word

print(text.find("Python")) # Return starting index

# 6. count() – Count Occurrences

print(text.count("o"))

# 7. startswith() – Check Starting Word

print(text.startswith("  Hello"))

# 8. endswith() – Check Ending Word

print(text.endswith("Python  "))

# 9. split() – Split String into List

print(text.split())

# 10. join() – Join List into String

words = ["Hello", "Python"]
print(" ".join(words))

# 11.  caoitalize() - Capitalize first character

texts = "aman"
print(texts.capitalize())