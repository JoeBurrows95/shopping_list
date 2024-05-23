def category_sort(ingredient):
    if ingredient[1] == 'fresh':
        return 1
    elif ingredient[1] == 'chilled':
        return 2
    elif ingredient[1] == 'ambient':
        return 3
    elif ingredient[1] == 'drink':
        return 4
    elif ingredient[1] == 'frozen':
        return 5

with open('ingredients.txt', "r") as ingredients_file:
    ingredients = ingredients_file.read().split('\n')

    ingredient_list = []

    for item in ingredients:
        item = item.split(';')
        ingredient_list.append(item)

    ingredient_list.sort(key=category_sort)

    for ingredient in ingredient_list:
        print(f"{ingredient[0]} ({ingredient[1]})")



