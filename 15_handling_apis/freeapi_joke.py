import requests

def fetch_random_jokes_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        joke_data = data["data"]
        content = joke_data["content"]
        return content
    else:
        raise Exception ("Failed to fetch random jokes")
    
def main():
    try:
        content = fetch_random_jokes_freeapi()
        print(f"Joke of the day: {content}")
    except Exception as e:
       print(str(e))

if __name__ == "__main__":
    main()