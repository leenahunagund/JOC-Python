import random

account=0
lottery=random.randint(1,10)
while(1):
    bet=int(input("your bet from 1-10: "))
    if bet==lottery:
        account=account+900-100
    else:
        account=account-100
    print(account)