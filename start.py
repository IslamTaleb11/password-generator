# 1 - Import string module
# 2 - Store all characters in lists (upper/lower case, digists, punctuations)
# 3 - Take number of characters from users
# 4 - Make sure the number of characters is 6 or more
# 5 - Shuffle all lists
# 6 - Calculate 30% and 20% of number of characters
# 7 - Create password 60% letters and 40% digits and punctuations


import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)


characters_number = input("How many characters you want for the password?: ")

while True:
        try:
            characters_number = int(characters_number)
            if characters_number < 6 :
                print("You need at least 6 characters!")
                characters_number = input("Please enter again how many characters you want: ")
                

        
            else:
                break
    
        except:
            print("Please enter numbers only!")
            characters_number = input("How many characters you want for the password?: ")


random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)



part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:])


print(password)
















































































