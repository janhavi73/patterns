print("half pattern of stars(*):")
n=int(input("please enter the amount of rows:"))


for i in range(1,n+1):
    print(" " * (n-i) +"*" * i)
    