from classes import Meal, Ingredient

# def read_meal_data(meals_text_file):
#     with open(meals_text_file, "r") as text_file:
#         meal_data = text_file.read().split("\n")

#     meal_list = []


# Lists the meals available for the user to choose from
def list_meals(text_file):
    
    # Takes the meals from the text file and saves to 'meals' variable
    with open(text_file, "r") as meal_file:
        # When working, check to see if .readlines() achieves the same
        meals = meal_file.read().split('\n')
    
    # Meal names separated out from quantities and saved to list
    meal_names = []

    for meal in meals:
        meal = meal.split(';')
        meal_names.append(meal[0])

    # Display string is created and printed
    disp_str = "Here's all the Jollie meals:\n"

    for n, meal_name in enumerate(meal_names, 1):
        disp_str += f"{n}. {meal_name}\n"

    print(disp_str)

    # Also return the list of meal names for subsequent use in main.py
    return(meal_names)


# Allows the user to select a meal to add to add to the shopping list
def select_meal(meal_list, text_file):
    selection = int(input("Choose a meal by entering the corresponding number. \
Enter '0' to return to the main menu:\n"))

    # Loops through meal_list to find the meal matching the number entered
    for n, meal_name in enumerate(meal_list, 1):
        if selection == n:
            selection = meal_name
        elif selection == 0:
            return selection
    
    with open(text_file, "r") as meal_file:
        # When working, check to see if .readlines() achieves the same
        meals = meal_file.read().split('\n')

    # Separates the meal name, ingredients, units, quantities and appends to new list
    meals_and_ingredients = []

    for meal in meals:
        meal = meal.split(';')
        meal = [m for m in meal if m != ""]
        
        meals_and_ingredients.append(meal)

    # Finds a match for the meal name selected and returns the ingredients
    # for that meal
    for meal in meals_and_ingredients:
        if meal[0] == selection:
            selected_meal = meal[1::]

    return selected_meal
    

# Lists ingredients for a selected meal
def list_ingredients(selected_meal):
    
    ingredient_list = "\nIngredients:"
    
    # Splits every ingredient so ingredient, quantity and unit are separate 
    # list items. Formats in a string to be displayed and prints it
    for ingredient in selected_meal:
        split_ingredient = str(ingredient).split('-')
        
        ingredient_list += f"\n{split_ingredient[0]} - \
{split_ingredient[1]}{split_ingredient[2] if split_ingredient[2] != "n" else ""}"
        
    ingredient_list += "\n"

    print(ingredient_list)

# def add_meal(meal_name, text_file):
    
#     meal = Meal(meal_name)

#     # while loop to add all ingredients, breaks when the user enters 'N'
#     while True:
        
#         ingredient = input("Ingredient: ")

#         measure = input("Measurement Unit (n, g, ml): ")
#         quantity = int(input("Quantity: "))

#         add_another = input("Add another ingredient? Enter 'N' if that's \
# all of them, and press enter if there's more:\n")
#         if add_another == "N":
#             break

#         meal.ingredients += f"{ingredient}-{quantity}-{measure};"


#         # String with the meal name followed by ingredients, all separated by ';'
#     # to enable ease of splitting later
#     string = f"\n{meal.name};{meal.ingredients}"

#     # Adds the new meal to the meals.txt file
#     with open(text_file, "a") as meals_file:
#         meals_file.write(string)
    
#     print("This meal has now been added to the list of meals.")

# Enables the user to add a meal to the meal list 
def add_meal(meal_name, text_file):
    
    meal = Meal(meal_name)

    # while loop to add all ingredients, breaks when the user enters 'N'
    while True:
        
        ingredient = input("Ingredient: ")

        measure = input("Measurement Unit (n, g, ml): ")
        quantity = int(input("Quantity: "))

        category = input("""What category is this ingredient? Enter it as displayed:
Fresh
Chilled
Ambient
Drink
Frozen
                         
Category: 
""").lower()
        # NEED TO ADD DEFENSIVE PROGRAMMING FOR AN INVALID ENTRY

        meal.ingredients += f"{ingredient}-{quantity}-{measure};"

        add_ingredient(ingredient, category, "ingredients.txt")

        add_another = input("Add another ingredient? Enter 'N' if that's \
all of them, and press enter if there's more:\n")
        if add_another == "N":
            break


    # String with the meal name followed by ingredients, all separated by ';'
    # to enable ease of splitting later
    string = f"\n{meal.name};{meal.ingredients}"

    # Adds the new meal to the meals.txt file
    with open(text_file, "a") as meals_file:
        meals_file.write(string)
    
    print("This meal has now been added to the list of meals.")


def add_ingredient(ingredient, category, text_file):
    try:
        with open(text_file, "r") as ingredient_file:
            ingredients = ingredient_file.read().split('\n')
            for item in ingredients:
                item = item.split(';')
                if item[0] == ingredient and item[1] == category:
                    return
            
        with open(text_file, "a") as ingredient_file:
            ingredient_file.write(f"\n{ingredient};{category}")

    except FileNotFoundError:
        with open(text_file, "w") as ingredient_file:
            ingredient_file.write(f"{ingredient};{category}")
            return
        
    

    


    # for item in ingredients:
    #     item.split(';')
    #     if item[0] == ingredient:
    #         return
    
    # with open(text_file, "a") as ingredient_file:
    #     ingredient_file.write(f"\n{ingredient};{category}")
        

        


            

def category_sort(ingredient):
    if ingredient[-1] == 'fresh':
        return 1
    elif ingredient[-1] == 'chilled':
        return 2
    elif ingredient[-1] == 'ambient':
        return 3
    elif ingredient[-1] == 'drink':
        return 4
    elif ingredient[-1] == 'frozen':
        return 5
    else:
        return 10

# Adds ingredients from the selected meal to the shopping list
def add_to_shopping_list(shopping_list, selected_meal):
        
    # Loops through every ingredient in the selected meal and splits so the
    # ingredient name is accessible
    for ingredient in selected_meal:
        split_ingredient = ingredient.split('-')
        # not_listed = False
        not_listed = True

        if shopping_list:

            # Loops through every item in the shopping list and splits so the
            # ingredient name is accessible
            for i, item in enumerate(shopping_list):
                split_item = item.split('-')

                # If the new ingredient is already in the shopping list, the 
                # quantity is added to the existing quantity instead of creating
                # a duplicate line item
                if split_ingredient[0] == split_item[0]:
                    split_item[1] = int(split_item[1]) + int(split_ingredient[1])
                    shopping_list[i] = f"{split_item[0]}-{split_item[1]}-{split_item[2]}"
                    not_listed = False

                    # continue
                
                # If it's not already listed, a new item will be added
                # else:
                #     not_listed = True
                    

            if not_listed == True:
                shopping_list.append(ingredient)

        else:
            shopping_list.append(ingredient)
    
    return shopping_list


def order_shopping_list(shopping_list, text_file):
    
    with open(text_file, "r") as ingredients_file:
        ingredients = ingredients_file.read().split('\n')

        ingredient_list = []

        for ingredient in ingredients:
            ingredient = ingredient.split(';')
            ingredient_list.append(ingredient)  
            
            
    shopping_list.sort()

    for item in shopping_list:
        item.pop()

    return shopping_list

    #     # Loops through the shopping list items and displays them in a user-friendly 
    # # format
    # for ingredient in shopping_list:
    #     ingredient = ingredient.split('-')
    #     if ingredient[2] == 'n':
    #         ingredient[2] = ''
        
    #     # Need to work out how to get the formatting consistently aligned
    #     # disp_str += f"{ingredient[0]}\t\t {ingredient[1]}{ingredient[2]}\n"
    #     disp_str += f"{ingredient[1]}{ingredient[2]}\t{ingredient[0]}\n"

    # print(disp_str)   


# Displays the user's up to date shopping list

# ADD HANDLING FOR IF THE SHOPPING LIST IS EMPTY
def display_shopping_list(shopping_list, text_file):
    
    disp_str = "Shopping List:\n"

    ordered_shopping_list = []

    # Loops through the shopping list items and displays them in a user-friendly 
    # format
    for ingredient in shopping_list:
        ingredient = ingredient.split('-')
        if ingredient[2] == 'n':
            ingredient[2] = ''
        
        ordered_shopping_list.append(ingredient)

    with open(text_file, "r") as ingredients_file:
        ingredients = ingredients_file.read().split('\n')

        ingredient_list = []

        for ingredient in ingredients:
            ingredient = ingredient.split(';')
            ingredient_list.append(ingredient)

    for i, item in enumerate(ordered_shopping_list):
        for ingredient in ingredient_list:
            if item[0] == ingredient[0]:
                ordered_shopping_list[i].append(ingredient[1])
                
    
    ordered_shopping_list.sort(key=category_sort)

    for i, ingredient in enumerate(ordered_shopping_list):
        if ingredient[-1] != ordered_shopping_list[i - 1][-1]:
            disp_str += f"\n---------------\n"
        disp_str += f"{ingredient[1]}{ingredient[2]}\t{ingredient[0]}\n"

    print(disp_str)
        

def add_shopping_list_item(shopping_list):

    # LATER, ADD DEFENSIVE PROGRAMMING FOR IF THE INGREDIENT ALREADY EXISTS
    ingredient = input("Ingredient: ")

    measure = input("Measurement Unit (n, g, ml): ")
    quantity = int(input("Quantity: "))

    category = input("""What category is this ingredient? Enter it as displayed:
Fresh
Chilled
Ambient
Drink
Frozen
                         
Category: 
""").lower()

    new_item = f"{ingredient}-{quantity}-{measure}"

    add_ingredient(ingredient, category, "ingredients.txt")

    shopping_list.append(new_item)

    print("This item has been added to your shopping list.\n")
    return shopping_list

# NEED TO ADD DEFENSIVE PROGRAMMING FOR IF THE LIST IS EMPTY
def edit_item_quantity(shopping_list):
    enumerated_string = ""

    for index, item in enumerate(shopping_list, 1):
        split = item.split('-')
        enumerated_string += f"{index}. {split[0]}\n"

    print("Which item would you like to edit?")
    # ADD DEFENSIVE PROGRAMMING FOR IF A NUMBER ISN'T ENTERED
    item_selection = int(input(enumerated_string))

    for index, item in enumerate(shopping_list, 1):
        if index == item_selection:
            index -= 1
            break

    # ADD DEFENSIVE PROGRAMMING FOR IF IT ISN'T A NUMBER
    new_quantity = int(input("Please enter the new quantity:\n"))
    
    split_item = shopping_list[index].split('-')
    split_item[1] = new_quantity

    updated_item = f"{split_item[0]}-{split_item[1]}-{split_item[2]}"

    shopping_list[index] = updated_item
    print("The quantity of this ingredient has been updated in your shopping list.\n")
    return shopping_list


def remove_shopping_list_item(shopping_list):
    enumerated_string = ""

    for index, item in enumerate(shopping_list, 1):
        split = item.split('-')
        enumerated_string += f"{index}. {split[0]}\n"

    print("Which item would you like to remove?")

    # ADD DEFENSIVE PROGRAMMING FOR IF A NUMBER ISN'T ENTERED
    item_selection = int(input(enumerated_string))

    for index, item in enumerate(shopping_list, 1):
        if index == item_selection:
            shopping_list.remove(item)
            break
    
    print("This item has been removed from your shopping list.\n")
    return shopping_list



