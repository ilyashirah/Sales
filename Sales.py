print("Gift Shop Sales Program")

staffname = input("Please input your name: ")
staffID = input("Please input your staff ID: ")

dateList = []
timeList = []
productList = []
priceList = []

while True:
    date = input("Enter the date of sales: ")
    time = input("Enter the time of sales: ")
    product = input("Enter the product name: ")
    price = float(input("Enter the product sales amount: $"))

    dateList.append(date)
    timeList.append(time)
    productList.append(product)
    priceList.append(price)

    cmd = input("Do you want to enter another entry? [y/n]: ")
    if(cmd == 'n'):
        break

total = 0
for i in range(len(priceList)):
    total += priceList[i]
    
total = sum(priceList)
average = total/len(priceList)
highsale = max(priceList)
indexhighsale = priceList.index(highsale)
highsaleproduct = productList[indexhighsale]

print(f"Staff name: {staffname}")
print(f"Staff ID: {staffID}")
print(f"Total sales amount: ${total}")
print(f"Average sales amount: ${average}")
print(f"Highest sales product: {highsaleproduct}")
print(f"Highest sales amount: ${highsale}")
