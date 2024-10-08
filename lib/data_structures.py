spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_list = [k.get('name') for k in spicy_foods]
    return spicy_list

def get_spiciest_foods(spicy_foods):
    foods = [k for k in spicy_foods if k['heat_level'] >5]
    return foods

def print_spicy_foods(spicy_foods):
    heat_sign = "🌶"
    if spicy_foods != None:
        for food in spicy_foods:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level']*heat_sign}")
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    heat_sign = "🌶"
    if spicy_foods != None:
        for food in spicy_foods:
            if(food['heat_level'] > 5):
                print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * heat_sign}")

def get_average_heat_level(spicy_foods):
    list_len = len(spicy_foods)
    avg_num = 0
    for k in spicy_foods:
        avg_num += k['heat_level']
    return avg_num/list_len

def create_spicy_food(spicy_foods, spicy_food):
    list_copy = spicy_foods
    list_copy.append({"name": spicy_food['name'], "cuisine": spicy_food['cuisine'], "heat_level": spicy_food['heat_level']})
    return list_copy
