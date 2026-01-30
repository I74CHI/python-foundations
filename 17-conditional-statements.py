"""CONDITIONAL STATEMENTS"""
# Conditional statements are used to make decisions in a program.
#   They tell Python : "If this condition is true, do this. Otherwise, do something else."
#   The indentation is of 4 spaces or a tab which is ultimatily 4 spaces.


"""1. if Statement"""
# Used when you want to run code only if a condition is true

age = 18
if age >=18:
    print("You can vote.")


"""2. if-else Statement"""
# Used when there are two choices.

age = 15
if age >=18:
    print("You can vote")
else:
    print("You cannot vote")

# Same as above
result = "You can vote" if age>=18 else "You cannot vote"
print(result)


"""3. if-elif-else Statement"""
# Used when there are more than two conditions.
# All if statement will be checked if there are multiple.
# The elif statement will get checked if and only if the if statement is false.

marks = 75
if marks >=90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


"""4. Nested if-else Statement"""
# A nested if-else means an if-else inside another if-else.
# It is used when decisions depend on multiple conditions.

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Too young")


"""5. Match-Case Statement"""
# The match-case statement is used when you want to compare one value with many possible options.
# It works like a switch statement in other languages.

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invaild day")
