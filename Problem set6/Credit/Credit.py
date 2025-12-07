from cs50 import get_string

number = get_string("Number: ")
length = len(number)

sum_doubled = 0
sum_others = 0

for i in range(length - 2, -1, -2):
    digit = int(number[i]) * 2
    sum_doubled += (digit // 10) + (digit % 10)

for i in range(length - 1, -1, -2):
    sum_others += int(number[i])

total = sum_doubled + sum_others

if total % 10 == 0:
    if length == 15 and (number.startswith("34") or number.startswith("37")):
        print("AMEX")
    elif length == 16 and number[:2] in ["51", "52", "53", "54", "55"]:
        print("MASTERCARD")
    elif (length == 13 or length == 16) and number.startswith("4"):
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")