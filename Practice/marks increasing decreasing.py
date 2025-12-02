a,b,c=tuple(map(int,input("enter the marks:").split()))

if a<=b and b<=c:
    print("increasing")

elif a>=b>=c:
    print("decreasing")

else:
    print("fluctuating")
