#Author:Naccon
import random
print(r'''
 /$$   /$$                                                  
| $$$ | $$                                                  
| $$$$| $$  /$$$$$$   /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$$ 
| $$ $$ $$ |____  $$ /$$_____/ /$$_____/ /$$__  $$| $$__  $$
| $$  $$$$  /$$$$$$$| $$      | $$      | $$  \ $$| $$  \ $$
| $$\  $$$ /$$__  $$| $$      | $$      | $$  | $$| $$  | $$
| $$ \  $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$  | $$
|__/  \__/ \_______/ \_______/ \_______/ \______/ |__/  |__/
''')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("""🔐 Welcome to the Python Password Generator!
Let's build a strong, customized password just for you. 🚀""")
input_1=int(input("Letters: "))
input_2=int(input("Numbers: "))
input_3=int(input("Symbols:"))
value=[]
pick =random.choice
for char in range(1,input_1+1):
    value.append(pick(letters))
for char in range(1,input_2+1):
    value.append(pick(numbers))
for char in range(1,input_3+1):
    value.append(pick(symbols))
print(f"Characters before shuffle: {value}")
random.shuffle(value)
print(f"Characters after shuffle: {value}")
x=""
for char in value:
    x+=char
print(f"🔐 Your generated password is: {x}")