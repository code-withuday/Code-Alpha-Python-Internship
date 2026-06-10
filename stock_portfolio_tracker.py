stocks = {
    "tata" : 380,
    "bmw" : 7488,
    "mercedes_benz" : 5176,
    "cooper" : 6480,
    "volkswagen" : 9581,
    "rolls royce" : 1237,
    "tesla" : 396,
    "toyota" : 2814,
    "maruti_suzuki" : 13072,
    "ford" : 1428  
}

total = 0

stock_name = input("enter stock name: ")
quantiity = int(input("enter quantity: "))

if stock_name.lower() in stocks:
    total = stocks[stock_name.lower()] * quantiity
    print("total investment: ", total)

else:
    print("stock not found")