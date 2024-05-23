import functions
from classes import Meal

def main():


    # with open("meals.txt", "r") as meals_file:
    #     meal = (meals_file.read())

    options = """What would you like to do?
1. View meals and their ingredients
2. Add a meal to the meal list
3. Select a meal to add to the shopping list
4. View shopping list
5. Edit shopping list

0. Exit
"""

    edit_options = """How would you like to edit the shopping list?
1. Add an item
2. Edit the quantity of an item
3. Remove an item
4. Swap an item

"""


    shopping_list = []

    print("Welcome to the Jollie Shopping List generator!")

    while True:
        option_selection = input(options)
        
        try:
            option_selection = int(option_selection)
        except ValueError:
            print("Please enter a numeric value")
            continue


        # View meals and their ingredients
        if option_selection == 1:
            meal_list = functions.list_meals("meals.txt")
            meal_selection = functions.select_meal(meal_list, "meals.txt")
            
            if meal_selection == 0:
                continue

            functions.list_ingredients(meal_selection)

            # User can add the meal's ingredients to their shopping list
            add_to_shopping_list = input("Would you like to add the ingredients\
 for this meal to the shopping list? (y/n)\n")
            
            if add_to_shopping_list == 'y':
                shopping_list = functions.add_to_shopping_list(shopping_list, meal_selection)
                print(f"The ingredients for the selected meal have been added \
to your shopping list.\n")


        # Add a meal to the meal list
        elif option_selection == 2:
            meal_name = input("Please enter the name of the meal:\n")

            functions.add_meal(meal_name, "meals.txt")
            functions.list_meals("meals.txt")  


        # Select a meal to add to the shopping list
        elif option_selection == 3:
            meal_list = functions.list_meals("meals.txt")
            print("\nWhich meal would you like to add to the shopping list?")

            meal_selection = functions.select_meal(meal_list, "meals.txt")

            if meal_selection == 0:
                continue

            shopping_list = functions.add_to_shopping_list(shopping_list, meal_selection)
            print(f"The ingredients for the selected meal have been added \
to your shopping list.\n")
            # functions.display_shopping_list(shopping_list)


        elif option_selection == 4:
            functions.display_shopping_list(shopping_list, 'ingredients.txt')

            input("\n\nPress enter to return to the main menu\n")


        elif option_selection == 5:
            # NEED TO ADD IN DEFENSIVE PROGRAMMING FOR IF A NUMBER ISN'T ENTERED
            # OR IF AN INVALID NUMBER IS ENTERED
            edit_choice = int(input(edit_options))

            if edit_choice == 1:
                shopping_list = functions.add_shopping_list_item(shopping_list)

            elif edit_choice == 2:
                shopping_list = functions.edit_item_quantity(shopping_list)

            elif edit_choice == 3:
                shopping_list = functions.remove_shopping_list_item(shopping_list)

            elif edit_choice ==4:
                shopping_list = functions.remove_shopping_list_item(shopping_list)
                print("What would you like to replace it with?")
                shopping_list = functions.add_shopping_list_item(shopping_list)
        

        # Exit
        elif option_selection == 0:
            print("Bye for now!")
            exit()


        else:
            print("Please select a valid option.")


if __name__ == "__main__":
    main()



