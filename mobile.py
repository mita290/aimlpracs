mobileprices=[12345,23456,45678,89076]
i=0
print(mobileprices,"\n")
for p in mobileprices:
    mobileprices[i]=float(p)
    i=i+1
print(mobileprices,"\n")
mobileprices.append(13999.0)
print(mobileprices,"\n")
print(mobileprices[::-1])
mobileprices.sort(reverse=True)
print(mobileprices,"\n")
mobileprices = [price * 1.18 for price in mobileprices]
print(mobileprices,"\n")
print("average=",sum(mobileprices)/len(mobileprices))