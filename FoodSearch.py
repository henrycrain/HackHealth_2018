#Searches foods dictionary

import Foods
import menu


active = 1
TotalCalories = 0
TotalFat = 0
TotalSodium = 0
TotalCarbs = 0
TotalProtein = 0
menu.menu()
while active != 0:
    print()
    foodin = input("Enter food, type done when finished: ")
    if foodin != "done":
        if foodin in Foods.foods:
            healthlist = Foods.foods[foodin]
            TotalCalories += healthlist[0]
            TotalFat += healthlist[1]
            TotalSodium += healthlist[2]
            TotalCarbs += healthlist[3]
            TotalProtein += healthlist[4]
        else:
            print("Invalid food")
    else:
        active = 0

print()
print("Total Calories: ", TotalCalories, "Calories")
print("Total Fat: ", TotalFat, "g")
print("Total Sodium: ", TotalSodium, "mg")
print("Total Carbs: ", TotalCarbs, "g")
print("Total Protein: ", TotalProtein, "g")
print()


