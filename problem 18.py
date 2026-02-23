d1 = {'apple':10, 'orange':20}
d2 = {'orange':30, 'banana':40}
for key, value in d2.items():
    if key in d1:
        d1[key] += value
    else:
        d1[key] = value
print(d1)