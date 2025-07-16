import requests

def fetch_random_book_freeapi():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        book_data = data["data"]
        initial_data = book_data["volumeInfo"]
        author = initial_data["authors"][0]
        category = initial_data["categories"][0]
        pages = initial_data["pageCount"]
        title = initial_data["title"]
        return author, category, pages, title
    else:
        raise Exception ("Failed to fetch random books")
    
def main():
    try: 
        author, category, pages, title = fetch_random_book_freeapi()
        print(f"Title: {title} \nAuthor: {author} \nCategory: {category} \nTotal Pages: {pages}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()