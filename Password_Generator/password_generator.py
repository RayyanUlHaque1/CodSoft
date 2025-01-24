import random
import string

def generate_password(length, special_char):
    print('Password-Generator')
  
    # Define the set of characters
    characters = string.ascii_letters + string.digits  # Letters (uppercase + lowercase) and digits
    if special_char:
        characters += string.punctuation  # Add special characters if selected
    
    # Generate the password by choosing random characters
    password = ''.join(random.choices(characters, k=length))  # Specify k for length
    return password

def main():
    # Get user input for password length .
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length should be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid Input.")
    
    # Special characters in the password
    special_char_input = input("Do you want to include special characters? (yes/no): ").strip().lower()
    special_char = special_char_input == "yes"  
    
    # Generate the password
    password = generate_password(length, special_char)
    
    # Print the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
