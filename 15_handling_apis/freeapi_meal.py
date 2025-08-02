import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/meals/meal/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        meal_name = user_data["strMeal"]
        meal_area = user_data["strArea"]
        meal_category = user_data["strCategory"]
        return meal_name, meal_area, meal_category
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        meal_name, meal_area, meal_category = fetch_random_user_freeapi()
        print(f"Name of meal: {meal_name} \nMeal origin: {meal_area} \nMeal category: {meal_category}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()