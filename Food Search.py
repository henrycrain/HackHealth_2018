#Searches foods dictionary
import Foods
active = 1
TotalCalories = 0
TotalFat = 0
TotalSodium = 0
TotalCarbs = 0
TotalProtein = 0
while active != 0:
    foodin = input("Enter food, type DONE when finished: ")
    if foodin != "DONE":
        healthlist = Foods.foods[foodin]
        TotalCalories += healthlist[0]
        TotalFat += healthlist[1]
        TotalSodium += healthlist[2]
        TotalCarbs += healthlist[3]
        TotalProtein += healthlist[4]
    else:
        active = 0


print(TotalCalories, TotalFat, TotalSodium, TotalCarbs, TotalProtein)


