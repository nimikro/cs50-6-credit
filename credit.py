from cs50 import get_int
import re

card = str(get_int("Number: "))

if len(card) < 13:
    print("INVALID")

sum_even = sum_odd = 0

for i in range(len(card)-2, -1, -2):
    digit = int(card[i])*2
    if digit >= 10:
        sum_even += int(digit / 10) + (digit % 10)
    else:
        sum_even += digit

for i in range(len(card)-1, -1, -2):
    digit = int(card[i])
    sum_odd += digit

final_sum = sum_even + sum_odd

if((final_sum % 10) != 0):
    print("INVALID")
else:
    if(re.match("34", card) or re.match("37", card)):
        print("AMEX")
    elif(re.match("4", card)):
        print("VISA")
    elif(re.match("51", card) or re.match("52", card) or re.match("53", card) or re.match("54", card) or re.match("55", card)):
        print("MASTERCARD")

