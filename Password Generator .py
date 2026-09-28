import random
import string

# Ask the user for password length
length = int(input("Enter password length: "))

# Character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
special = string.punctuation

# Make sure the password contains all required character types
password = [
    random.choice(uppercase),
    random.choice(lowercase),
    random.choice(numbers),
    random.choice(special)
]

# Combine all character sets
all_characters = uppercase + lowercase + numbers + special

# Generate remaining characters
for _ in range(length - 4):
    password.append(random.choice(all_characters))

# Shuffle the password so the character types aren't predictable
random.shuffle(password)

# Convert list to string
password = ''.join(password)

# Display the password
print("\nGenerated Strong Password:", password)