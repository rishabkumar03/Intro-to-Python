import requests

def fetch_random_product_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        product_data = data["data"]
        description = product_data["description"]
        price = product_data["price"]
        title = product_data["title"]
        return description, price, title
    else:
        raise Exception ("Failed to fetch product data")
    
def main():
    try:
        description, price, title = fetch_random_product_freeapi()
        print(f"Title: {title} \nDescription: {description} \nPrice: ${price}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()