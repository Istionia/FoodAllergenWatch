import requests
from bs4 import BeautifulSoup

def scrape_serious_eats_recipes_by_country(country):
    # Base URL for searching recipes on Serious Eats
    base_url = "https://www.seriouseats.com/search"
    
    # Set up the query parameters
    params = {
        'term': country.lower()  # Convert country name to lowercase
    }
    
    # Make the request to Serious Eats
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print(f"Failed to retrieve data for {country}")
        return []
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find recipe cards in the search results
    recipe_elements = soup.find_all('article', class_='card')
    
    # List to store the extracted recipe information
    recipes = []
    
    for recipe in recipe_elements:
        title = recipe.find('h4', class_='heading-content').text.strip()
        link = recipe.find('a', class_='card-asset-link')['href']
        full_link = f"https://www.seriouseats.com{link}"
        
        # Fetch the detailed recipe page for ingredients
        recipe_response = requests.get(full_link)
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
            'link': full_link
        })
    
    return recipes
