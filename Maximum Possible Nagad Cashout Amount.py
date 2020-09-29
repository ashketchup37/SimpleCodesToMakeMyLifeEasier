#Take the Current Balance as an input
current_balance = float(input("Current Balance: "))

#As you have to cashout whole taka
available = int(current_balance)

#In Brief, My algorith works like this:
#Everytime available money plus its charge is bigger than current balance, my available money gets smaller by 1 taka.

while 1:
    if available < 10000:
        charge = 1.75 / 100
    else:
        charge = 1.6 / 100
    if current_balance < (available + (available * charge)):
        available -= 1
    else:
        break

print(available)
