print(" *** Divisible number ***")
y = int(input("Enter a positive number : "))

def div(x):
    a = 0
    l = []
    if x == 0:
        print("0 is OUT of range !!!")
    else:
        for i in range(1,x):
            if x % i == 0:
                a += 1
                l.append(i)
                
        return x,a+1,l


number = div(y)[2]
num = number.append(y)

print("Output ==>",*number, sep = ' ')
print("Total ==> " + str(div(y)[1]))