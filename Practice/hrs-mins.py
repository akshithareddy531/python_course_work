hrs,mins= tuple(map(int,input("enter the time (HH:MM): ").split(':')))

if 0<=hrs<24 and 0<=mins<60:
    print("valid time")
else:
    print("invalid time")


number= input("enter the number: ")
n=len(number)
if number%2==0:
    l=list(map(int,number))
    if sum(l[:n//2])==sum(1[n//2:]):
        print("lucky number")
    else:
        print("unlucky number")

else:
    print("unlucky number")
