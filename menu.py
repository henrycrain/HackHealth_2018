import Foods

def menu():
    print("Menu:")
    for food in Foods.foods:
        print(food)

    print("Enter all foods you ate today (enter done when finished:")

    foods = []
    food = input()
    while food != "done":
        foods.append(food)
        food = input()

    return foods