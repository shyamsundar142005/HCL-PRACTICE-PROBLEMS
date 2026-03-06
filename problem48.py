card = input("Enter credit card number: ")
masked = "*" * (len(card) - 4) + card[-4:]
print("Masked number:", masked)