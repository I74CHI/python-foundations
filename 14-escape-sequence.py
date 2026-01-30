# ESCAPE SEQUENCE
"""
Escape characters are used to put special characters inside a string. These characters are hard or not allowed to type normally. They start with a backslash (\), which tells Python to treat the next character in a special way. Escape characters are mainly used to:

• move text to a new line or add spaces
• use quotes inside a string
• write file paths
• add special control characters
"""


# 1. \n (Newline)
#   Breaks the string into a new line.

print("Hello, World!\nWelcome to Python.")


# 2. \t (Tab)
#   The \t escape character inserts a tab space between words or characters.

print("Name\tAge\tLocation")


# 3. \\ (Backslash)
#   The \\ escape character inserts a literal backslash in the string.

print("This is a backslash: \\")


# 4. \' (Single Quote)
#   The \' escape character allows you to insert a single quote within a string that is enclosed by single quotes.

print('It\'s a great day!')


# 5. \" (Double Quote)
#   The \" escape character allows you to insert a double quote within a string that is enclosed by double quotes.

print("He said, \"Hello!\"")


# 6. \r (Carriage Return)
#   The \r escape character moves the cursor to the beginning of the line. It can overwrite the existing text.

print("Hello, World!\rHi")


# 7. \b (Backspace)
#   The \b escape character moves the cursor one character back, effectively deleting the last character.

print("Hello, World!\b")


# 8. \f (Form Feed)
#   The \f escape character moves the cursor to the next page (less commonly used in modern programming).

print("Hello\fWorld!")


# 9. \v (Vertical Tab)
#   The \v escape character moves the cursor vertically (less commonly used).

print("Hello\vWorld!")


# 10. \xhh (Hexadecimal)
#   The \xhh escape character represents a character using its hexadecimal value hh.

print("Hello \x48\x65\x6C\x6C\x6F")
