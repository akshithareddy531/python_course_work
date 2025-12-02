products=['laptop','mouse','keypad','speakers','watch']
search=input("enter the product:").strip()
for i in products:
    if i==search:
        print("product found!shop now")
        break
    print(i)
else:
    print("end of the product. The item you search for is not found")
