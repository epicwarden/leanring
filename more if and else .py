good_credit = False
house_price = 1000000
down_payment = int(house_price / 10)
down_payment2 = int(house_price / 5)
if good_credit:
    print(" they will need 10%")
    print(f'you will need to pay {down_payment}')
else:
    print("they will need 20%")
    print(f'you will need to pay {down_payment2}')
