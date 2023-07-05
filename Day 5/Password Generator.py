
import random



print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Basically, I want to have each different data type be added randomly to the final password, final appraoch was to

def password_gen(L,S,N):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    temp_password = ""
    total_char = L+S+N
    for i in range(L):
        temp_password += random.choice(letters)
    for i in range(S):
        temp_password += random.choice(symbols)
    for i in range(N):
        temp_password += random.choice(numbers)
    return ''.join(random.sample(temp_password,k=total_char))


print(password_gen(nr_letters,nr_symbols,nr_numbers))
