income,credit,existing=map(int,input().split())
if(income>=50000 and credit>=700 and existing<=20000):
    print("Eligible")
elif(income>=30000 and credit>=600 and existing<=40000):
    print("Review")
else:
    print("Reject")
