
favorite_foods = []       # initialize empty list for favourite foods
while True:
    print("Favourite Foods Manager ")
    print("0. Exit")
    print("1. Add Foods")
    print("2. Remove Foods")
    print("3. View Favourite All Foods")

    choice = input("Choose an option: ") # from taken user input

    if choice == "0":
        print("Thanks for using Favourite Foods Manager")
        break
    elif choice == "1":
        food = input("Enter you favourite food name: ")
        favorite_foods.append(food)
        print(f"{food} added Successfully")

    elif choice == "2":
        food = input("Enter a food name which you want to remove: ")
        if food in favorite_foods:
            favorite_foods.remove(food)
            print(f"{food} remove Successfully")
 
        else:
            print(f"{food} food does not exists in list ")

    elif choice == "3":
        if favorite_foods:
            print("Your favourite foods: ")
            for index, food in enumerate(favorite_foods, start=1):
                print(f"{index}.{food}")
        else:
            print("Food List is empty or didn't added yet")
    else:
        print("Invalid Choice!")
