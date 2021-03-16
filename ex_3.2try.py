hrs=input("Enter the hours ")
rate=input("enter the rate ")
try:
    h=float(hrs)
    r=float(rate)
except:
    print("error please enter numeric value")
    quit()
if h>40:
    pay=h*r
    inc=(h-40)*(r*0.5)
    p=pay+inc
    
else:
    pay=h*r
print(p)