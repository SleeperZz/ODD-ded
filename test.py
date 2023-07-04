a,b = (input("Enter your High and Weight : ")).split()

x = a / (b * b)
c = float(x)
if(c <= 18.50):
    print("Less weight")
elif(18.50 <= c <= 23.00) :
    print("Normal weight")
elif(23.00 <= c <= 25.00):
    print("More than normal weight")
elif(25.00 <= c <= 30.00):
    print("Getting fat")
elif(c >= 30):
    print("Fat")

