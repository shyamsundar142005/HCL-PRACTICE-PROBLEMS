def password_checker(password=""):
    score=0
    if len(password)>=8:
        score+=1

    if any(ch.isdigit() for ch in password):
        score+=1
    if any(ch.isupper() for ch in password):
        score+=1
    if any(ch.islower() for ch in password):
        score+=1
    if any(ch.isalnum() for ch in password):
        score+=1
    return score

s=password_checker(input("Enter Password: "))
print(s)
