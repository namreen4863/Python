hrs=input("Enter the hours ")
h=float(hrs)
rate=input("enter the rate ")
r=float(rate)
if h>40:
    pay=h*r
    inc=(h-40)*(r*0.5)
    p=pay+inc
    
else:
    pay=h*r
print(p)