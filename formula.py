# accepting user input parameter and displaying on console
def bmr_calc(weight, height, age, sex):
    if sex == 'm':
        return 655 + (4.35 * float(weight)) + (4.7 * float(height)) - (4.7 * float(age))
    elif sex == 'f':
        return 66 + (6.23 * float(weight)) + (12.7 * float(height)) - (6.8 * float(age))


def kcal_maintain(bmr, activity):
    if activity == "1":
        return float(bmr) * 1.2
    elif activity == "2":
        return float(bmr) * 1.375
    elif activity == "3":
        return float(bmr) * 1.55
    elif activity == "4":
        return float(bmr) * 1.725
    elif activity == "5":
        return float(bmr) * 1.9


print("We will now calculate the amount of calories required to maintain your weight.")
print()
user_sex = input("Are you male (enter 'm') or female (enter 'f')?")
user_sex.lower()
if user_sex != 'm' and user_sex != 'f':
    print("Invalid user input.")
user_weight = input('What is your weight, in pounds?')
user_height = input("What is your height, in inches?")
user_age = input('What is your age, in years?')
user_bmr = bmr_calc(user_weight, user_height, user_age, user_sex)


user_activity = input('On a scale of 1 to 5, how active are you?')
print()

x = kcal_maintain(user_bmr, user_activity)

print("In order to lose one pound per week, you should consume %d Calories per day" % int(round(x-500)))
print("In order to lose half a pound per week, you should consume %d Calories per day" % int(round(x-250)))
print("In order to maintain your weight, you should consume %d Calories per day" % x)
print("In order to gain half a pound per week, you should consume %d Calories per day" % int(round(x+250)))
print("In order to gain one pound per week, you should consume %d Calories per day" % int(round(x+500)))
print()
