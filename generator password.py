import string
import random

#def generaor_password()-> :
s = list()
n = int(input('Количество символов:'))
for i in range(n):
    k = random.choice(string.ascii_letters)
    s += k 
s = str(s)
print(s)
