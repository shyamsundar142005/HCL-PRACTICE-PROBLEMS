l1=list(input().split(","))

striped=list(map(lambda x: " ".join(x.strip().split()).title(),l1))
print(striped)