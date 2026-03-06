card = input("Enter credit card number: ")
maske = "*" * (len(card) - 4) + card[-4:]
print("Masked number:", maske)