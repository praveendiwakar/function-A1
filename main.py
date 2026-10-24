def greet_customer():
    print("welcome to the lemonade stand!")
    print("please place your order")

greet_customer()

price_percup = float(input("enter the price per cup:"))
number_ofcups = int(input("enter the numbeer of cups purchased:"))

def calculate_total(price,cups):
    total = price*cups
    return total

total = calculate_total(price_percup, number_ofcups)
round_total = round(total)
print(round_total)

amount_paid = int(input("enter the amount paid:"))

def calculate_change(amount,total):
    change = amount - total
    return change

change = calculate_total(amount_paid, round_total)

def thankyou_message(cups):
    if cups >= 5:
        return "wow big order thanks for visiting"
    else:
        return "thanks for visiting"
message = thankyou_message(number_ofcups)

print("your final receipt")
print("price per cup:", price_percup)
print("number of cups ordered:", number_ofcups)
print("amount paid:", amount_paid)
print("change to be paid:",change )
print(message)





