hrs=input("Enter the hours ")
h=float(hrs)
rate=input("enter the rate ")
r=float(rate)
def computepay(h,r):
    if h>40:
        pay=h*r
        inc=(h-40)*(r*0.5)
        p=pay+inc
        return p
    else :
        pay=h*r
        return pay
p=computepay(h,r)
print("Pay",p)