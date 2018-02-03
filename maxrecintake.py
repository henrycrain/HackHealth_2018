import formula
import FoodSearch

max_fat = 65 * formula.x / 2000
#grams

max_sodium = 2400 * formula.x / 2000
#mg

max_carbs = 300 * formula.x / 2000
#grams

max_protein = 50 * formula.x / 2000
#grams


if max_fat < FoodSearch.TotalFat:
    print("Max recommended Fat: ", max_fat, "g - You are over your recommended daily intake.")
else:
    print("Max recommended Fat: ", max_fat, "g")

if max_sodium < FoodSearch.TotalSodium:
    print("Max recommended Sodium: ", max_sodium, "mg - You are over your recommended daily intake.")
else:
    print("Max recommended Sodium: ", max_sodium, "mg")

if max_carbs < FoodSearch.TotalCarbs:
    print("Max recommended Carbs: ", max_carbs, "g - You are over your recommended daily intake.")
else:
    print("Max recommended Carbs: ", max_carbs, "g")

if max_protein < FoodSearch.TotalProtein:
    print("Max recommended Protein: ", max_protein, "g - You are over your recommended daily intake.")
else:
    print("Max recommended Protein: ", max_protein, "g")
