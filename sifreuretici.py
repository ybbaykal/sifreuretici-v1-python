import random
import string

print('Selam dünya! ben bir şifre üreticisiyim :) ')

length = int (input('\nŞifre uzunluğunu giriniz:'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print(password)
