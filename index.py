import requests

print("Enter a asset : ")
asset = input()

apiUrl = "https://api.coincap.io/v2/assets/" + asset

response = requests.get(apiUrl)

data = response.json()

print("What do you want?")
print("1.rank")
print("2.symbol")
print("3.price")
print("4.market cap")
print("5.volume")
print("6.change%")
value = input("Enter:")

if(value == "1"):
    value = "rank"
elif(value == "2"):
    value = "symbol"
elif(value == "3"):
    value = "priceUsd"
elif(value == "4"):
    value = "marketCapUsd"
elif(value == "5"):
    value = "volumeUsd24Hr"
elif(value == "6"):
    value = "changePercent24Hr"
else:
    print("invalid number")


price = data["data"][str(value)]

priceInt = float(price)
rounded_price = round(priceInt, 2)

print(rounded_price)