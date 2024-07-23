# Python program to ask for user's name and age, and print a greeting message

# Ask for the user's name
name = input("Enter your name: ")

# Ask for the user's age
age = int(input("Enter your age: "))

# Calculate the age next year
age_next_year = age + 1

# Print the greeting message
print(f"Hello, {name}! You are {age} years old now, and you will be {age_next_year} years old next year.")
