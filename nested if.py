card=True
PIN=True
if card:
    print("card accepted")
    if PIN:
        print("Transaction Successful")
card=True
PIN=False
if card:
    print("card accepted")
    if PIN:
        print("Transaction successful")
card=False
PIN=True
if card:
    print("card is accepted")
    if PIN:
        print("Transaction successful")
