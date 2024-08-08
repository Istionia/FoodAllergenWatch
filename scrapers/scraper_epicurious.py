"""
scraper_epicurious.py

This module provides functionality to scrape recipes from the Epicurious website based on the specified country cuisine.
It uses the BeautifulSoup library to parse HTML content and the requests library to handle HTTP requests.

Functions:
    scrape_epicurious_recipes_by_country(country): Scrapes recipes from Epicurious based on the specified country cuisine.

Usage Example:
    if __name__ == "__main__":
        country = 'french'
        recipes = scrape_epicurious_recipes_by_country(country)
        for recipe in recipes:
            print(recipe['title'])
            print(recipe['ingredients'])
            print(recipe['link'])
            print("---")
"""

import requests
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_epicurious_recipes_by_country(country):
    """
    Scrape recipes from Epicurious based on the specified country cuisine.

    Args:
        country (str): The name of the country cuisine to search for.

    Returns:
        list: A list of dictionaries containing recipe information.
    """
    base_url = "https://www.epicurious.com/search"
    params = {
        'content': 'recipe',
        'cuisine': country.lower()
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Failed to retrieve data for {country}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    recipe_elements = soup.find_all('article', class_='recipe-content-card')

    recipes = []
    for recipe in recipe_elements:
        title_element = recipe.find('h4', class_='hed')
        link_element = recipe.find('a')

        if not title_element or not link_element:
            continue

        title = title_element.text.strip()
        link = "https://www.epicurious.com" + link_element['href']

        try:
            recipe_response = requests.get(link)
            recipe_response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Failed to retrieve recipe details from {link}: {e}")
            ingredients_list = []
        else:
            recipe_soup = BeautifulSoup(recipe_response.text, 'html.parser')
            ingredients = recipe_soup.find_all('li', class_='ingredient')
            ingredients_list = [ingredient.text.strip() for ingredient in ingredients]

        recipes.append({
            'title': title,
            'ingredients': ingredients_list,
            'country': country,
            'link': link
        })

    return recipes

# Example usage
if __name__ == "__main__":
    country = 'malaysian'
    recipes = scrape_epicurious_recipes_by_country(country)
    for recipe in recipes:
        print(recipe['title'])
        print(recipe['ingredients'])
        print(recipe['link'])
        print("---")