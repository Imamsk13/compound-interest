p= int(input("enter principle amount"))
r= int(input("enter rate of interest"))
n= int(input("enter number of years"))
A=p*(1+(r/100))**n 
ci=A-p
print (A)
print (ci)