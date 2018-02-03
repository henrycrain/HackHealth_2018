# accepting user input parameter and displaying on console
def BMR_calc(weight, height, age, sex):
    if sex == 'm':
        return (655 + (4.35 * float(weight)) + (4.7 * float(height)) - (4.7 * float(age)))
    elif sex == 'f':
        return (66 + (6.23 * float(weight)) + (12.7 * float(height)) - (6.8 * float(age)))

def kcal_maintain(BMR, activity):
    if activity == "1":
        return (float(BMR) * 1.2)
    elif activity == "2":
        return (float(BMR) * 1.375)
    elif activity == "3":
        return (float(BMR) * 1.55)
    elif activity == "4":
        return (float(BMR) * 1.725)
    elif activity == "5":
        return (float(BMR) * 1.9)

def AskBMI()
    print ("We will now calculate the amount of calories required to maintain your weight.")
    sex = input("Are you male (enter 'm') or female (enter 'f')?")
    sex.lower()
    if sex != 'm' and sex!= 'f':
        print ("Invalid user input.")
    weight = input('What is your weight, in pounds?')
    height = input('What is your height, in inches?')
    age = input('What is your age, in years?')
    BMR = BMR_calc(weight, height, age, sex)
    return BMR


activity = input('On a scale of 1 to 5, how active are you?')

x = kcal_maintain(AskBMI,activity)

print ("In order to lose one pound per week, you smhould consume %f Calories per day" % (x-500))
print ("In order to lose half a pound per week, you should consume %f Calories per day" % (x-250))
print ("In order to maintain your weight, you should consume %f Calories per day" % x)
print ("In order to gain half a pound per week, you should consume %f Calories per day" % (x+250))
print ("In order to gain one pound per week, you should consue %f Calories per day" % (x+500))
