import requests

def fetch_random_stock_freeapi():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        stock_data = data["data"]
        name = stock_data["Name"]
        symbol = stock_data["Symbol"]
        current_price = stock_data["CurrentPrice"]
        return name, symbol, current_price
    else:
        raise Exception ("Failed to fetch random stocks")
    
def main():
    try:
        name, symbol, current_price = fetch_random_stock_freeapi()
        print(f"Name: {name} \nSymbol: {symbol} \nCurrent Price: {current_price}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()