num1 = int(input("enter 1st no")) 
num2 =int(input("enter 2nd no"))
def swap(n1 ,n2):
    n1 = n1-n2
    n2 = n2 + n1
    n1= n2-n1
    return (n1,n2)


print(swap(num1,num2))