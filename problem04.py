amount=int(input("Enter the amount: "))
if(amount<1000):
    print("Amount to pay: ",amount)
elif(amount>=1000 and amount<5000):
    diff=5/100
    discount=amount*diff
    print("Amount to pay: ",amount-discount)
else:
    diff = 10 / 100
    discount = amount * diff
    print("Amount to pay: ", amount-discount)
