# app/utils.py

big_9_allergens = [
    "peanut", "tree nut", "milk", "egg", "wheat", 
    "soy", "fish", "shellfish", "sesame"
]

def check_for_allergens(ingredients):
    """
    Checks if any of the ingredients contain the big 9 allergens.
    
    Parameters:
        ingredients (list): A list of ingredient strings.
        
    Returns:
        list: A list of detected allergens.
    """
    detected_allergens = []
    for allergen in big_9_allergens:
        for ingredient in ingredients:
            if allergen in ingredient.lower():
                detected_allergens.append(allergen)
                break
    return detected_allergens

