def main():
    welcome()
    gender = sex()
    weight = get_weight()
    height = get_height()
    age = get_age()
    resting_bmi = calculate_bmi(gender, weight, height, age) #calcluates resting bmi
    final_calculation(resting_bmi)

def welcome():
    print("Calculate your Body Mass Index (BMI)!\nFind out how many daily calories you need to maintain your current body weight.\n")

#calculate total daily calories based on bmi and and activity level
def final_calculation(resting_bmi):
    user_activity_lvl = get_user_activity()#ask for user activity level
    maintain = {"sedentary" : get_sedentary(resting_bmi) , "light" : get_light_activity(resting_bmi), "moderate" : get_moderate_activity(resting_bmi), "active" : get_very_active(resting_bmi)}
    if user_activity_lvl == "sedentary":
        print("You need to eat " + str(maintain["sedentary"]) + " calories a day to maintain your current weight")
    if user_activity_lvl == "light":
        print("You need to eat " + str(maintain["light"]) + " calories a day to maintain your current weight")
    if user_activity_lvl == "moderate":
        print("You need to eat " + str(maintain["moderate"]) + " calories a day to maintain your current weight")
    if user_activity_lvl == "active":
        print("You need to eat " + str(maintain["active"]) + " calories a day to maintain your current weight")

# ask user sex, rule out incorrect options
def sex():    
    sexes = ["male","female","M","F","f","m","Male","Female"]
    while True:
        sex = str(input("Do you identify as male or female? "))
        while sex not in sexes:
            sex = str(input("Please enter either 'male' or 'female' "))
        else:
            return sex
            break

#ask user weight in kg
def get_weight():
    weight_kg = float(input("Enter your weight in kg: "))
    while weight_kg <= 0:
        weight_kg = float(input("Invalid input. Please enter your weight in kg: "))
    else:
        return weight_kg

#ask user height in m
def get_height():
    height_m = float(input("Enter your height in cm: "))
    while height_m <= 0:
        height_m = float(input("Invalid input. Please enter your height in inches: "))
    else:
        return height_m

#ask user age in yrs
def get_age():
    age_yrs = int(input("Enter your age in years: "))
    while age_yrs <= 0:
        age_yrs = int(input("Invalid Input. Please enter your age in years: "))
    else:
        return age_yrs

#bmi calculations for male or female
def calculate_bmi(gender, weight, height, age):
    male = ["male", "M" , "m", "Male"]
    female = ["female", "F", "f", "Female"]
    if gender == female:
        women = weight/(height*height)
        return int(women)
    else:
        men = weight/(height*height)
        return int(men)

#get user weekly activity levels        
def get_user_activity():
    activity_lvl = ["sedentary", "light", "moderate", "active"]
    while True:
        user_lvl = str(input("\nWhat is your activity level?\n\nSedentary is little to no exercise.\nLightly active is 1 - 3 days/week.\nModerately active is 3 - 5 days/week.\nVery active is 6 - 7 days/week.\n\nPlease enter: 'sedentary', 'light', 'moderate',  or 'active' "))
        while user_lvl not in activity_lvl:
            user_lvl = str(input( "Invalid input. Please enter: 'sedentary', 'light', 'moderate',  or 'active' "))
        else:
            return user_lvl
            break

#pull resting bmi & multiply it for sedentary lvls
def get_sedentary(resting_bmi):
    sedentary = resting_bmi * 1.2
    return sedentary

def get_light_activity(resting_bmi):
    light = resting_bmi * 1.375
    return light

def get_moderate_activity(resting_bmi):
    moderate = resting_bmi * 1.55
    return moderate

def get_very_active(resting_bmi):
    active = resting_bmi * 1.725
    return active


if _name_ == '_main_':
    main()