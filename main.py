#Password Generator Project V2
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Şifre oluşturucuya hoş geldiniz.")
nr_letters= int(input("Şifreniz kaç harf içersin?\n")) 
nr_symbols = int(input(f"Kaç tane sembol içersin?\n"))
nr_numbers = int(input(f"Kaç tane sayı içersin?\n"))

password_list = []
for char in range(1 , nr_letters + 1):
  password_list += random.choice(letters)

for char in range(1 , nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1 , nr_numbers + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char
print(password)