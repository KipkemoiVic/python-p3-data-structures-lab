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
    return [food_name["name"] for food_name in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food_name for food_name in spicy_foods if food_name["heat_level"]>5]

def print_spicy_foods(spicy_foods):
    for food_name in spicy_foods:
        name = food_name["name"]
        cuisine = food_name["cuisine"]
        heat_level = food_name["heat_level"]
        heat_level_symbols = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_symbols}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food_name in spicy_foods:
        if food_name["cuisine"] == cuisine:
            return food_name

def print_spiciest_foods(spicy_foods):
     for food_name in spicy_foods:
        name = food_name["name"]
        cuisine = food_name["cuisine"]
        heat_level = food_name["heat_level"]
        heat_level_symbols = "🌶" * heat_level
        if heat_level > 5:
            print(f"{name} ({cuisine}) | Heat Level: {heat_level_symbols}")

def get_average_heat_level(spicy_foods):
    total_heat = 0
    foods= len(spicy_foods)
    for food_name in spicy_foods:
        total_heat += food_name["heat_level"]
    if foods > 0:
        average_heat_level = total_heat / foods
        return int(average_heat_level)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
