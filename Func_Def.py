#Function to add
def addtwo(a,b):
    added = a+b 
    return added

#Function to multiply
def multtwo(a,b):
    mult = a*b 
    return mult

#Function to divide
def divtwo(a,b):
    div = a/b 
    return div

#Function to subtract
def subtwo(a,b):
    sub = a-b 
    return sub

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
x = addtwo(n1,n2)
print("Sum =",x)
w=subtwo(n1, n2)
print("Diffrence =", w)
y = multtwo(n1, n2)
print("Product = ",y)
z = divtwo(n1, n2)
print("Division = ", z)
