import requests
from bs4 import BeautifulSoup

def scrape_epicurious_recipes_by_country(country):
    # Base URL for searching recipes on Epicurious
    base_url = "https://www.epicurious.com/search"
    
    # Set up the query parameters
    params = {
        'content': 'recipe',
        'cuisine': country.lower()  # Convert country name to lowercase
    }
    
    # Make the request to Epicurious
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print(f"Failed to retrieve data for {country}")
        return []
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find recipe cards in the search results
    recipe_elements = soup.find_all('article', class_='recipe-content-card')

    # List to store the extracted recipe information
    recipes = []
    
    for recipe in recipe_elements:
        title = recipe.find('h4', class_='hed').text.strip()
        link = "https://www.epicurious.com" + recipe.find('a')['href']
        
        # Fetch the detailed recipe page for ingredients
        recipe_response = requests.get(link)
        if recipe_response.status_code == 200:
            recipe_soup = BeautifulSoup(recipe_response.text, 'html.parser')
            ingredients = recipe_soup.find_all('li', class_='ingredient')
            ingredients_list = [ingredient.text.strip() for ingredient in ingredients]
        else:
            ingredients_list = []
        
        # Append the scraped data to the list
        recipes.append({
            'title': title,
            'ingredients': ingredients_list,
            'country': country,
            'link': link
        })
    
    return recipes

recipes = scrape_epicurious_recipes_by_country('french')
for recipe in recipes:
    print(recipe['title'])
    print(recipe['ingredients'])
    print(recipe['link'])
    print("---")