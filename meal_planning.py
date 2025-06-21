import random


#serving size calories, protein grams
#The intent of the program is for me to dedicate less time to thinking about what to eat
#The program will do it for me
#I just follow what it says


sweet = {
         'Greek Yogurt': [90, 16, 170],
         'Fiber One Cereal': [45, 2, 20],
         'Peanut Butter': [95, 8, 16],
         'Lite Maple Syrup': [25, 0, 15],
         'Orgain Protein Powder': [75, 10, 23],
         'Corn Flakes': [70, 2, 20],
         'PB2': [60, 6, 13]
}

savory = {

        'Avocado': [80, 0, 50],
         "Nature's Own Bread": [65, 4, 65],
         '3 Egg Whites': [50, 11, 100],
         'Cream Cheese': [60, 4, 31],
         'Bagel': [270, 10, 50],
         'Grilled Chicken': [100, 20, 84],
         'Two Eggs': [140, 12, 100]


}

salad = {
    'Lettuce': [15, 0],
    'Spinach': [23, 0],
    'Two Eggs': [140, 12],
    'Hummus': [100, 3],
    'Banana Peppers': [5, 0],
    'Red Peppers': [5, 0],
    'Feta Cheese': [80, 4, 28],
    'Butternut Squash': [60, 1], #140g is quite a bit! err on side of caution due to prep methods
    'Grilled Chicken': [100, 20],
    'Balsamic Vinegar': [10, 0]
}

snacks = {
    'Popcorners': [120, 3],
    'Pretzels': [100, 1],
    'Rice Krispie Treat': [90, 0],
    'Fruit Leather': [50, 0]}


cooked_food = {
    'Codfish Casserole': [150, 6, 50],
    'Chicken Breast': [130, 10, 70],
    'Chicken Thigh': [170, 10, 70],
    'Cocktail Patty': [110, 3, 50],
    'Rice': [130, 3, 100],
    'Mac and Cheese': [110, 3, 80],
    'Ackee': [100, 2, 50],
    'Cabbage': [50, 0, 80],
    'Fish': [150, 10, 50]
}

def serving_scaler(food_item: str, flavor: dict,  desired_cals: float):
    'return the grams required to get the food to a certain amount'
    scalar = desired_cals/flavor[food_item][0]
    #item, grams of protein, total grams
    return [food_item, flavor[food_item][1] * scalar, flavor[food_item][2] * scalar]

def meal_calculator(meal_type: dict, components: list):
    cal_count = 0
    protein_count = 0
    for food in components:
        cal_count += meal_type[food][0]
        protein_count += meal_type[food][1]
        
    return (cal_count, protein_count)


#Explaining the args
#flavor = dict of foods with a corresponding flavor profile
#calories = desired max calorie total for the meal
#precise = allows you to nail down servings to be exactly the calorie total
#base = food that you want to start the meal with
#no_thanks = food in the dictionary that you don't want in the final meal
def meal_creator(flavor: dict, calories: float, precise = False, base = None, no_thanks = None):
    'create a meal that has less than or equal to the specified calorie count'
    food_choices = list(flavor.keys())
    random.shuffle(food_choices)
    
    #Allow the user to specify a certain base for the meal 
    if base == None:
        cal_count =  0
        protein_count = 0
        meal = []
    else:
        cal_count = flavor[base][0]
        protein_count = flavor[base][1]
        meal = [base]
        food_choices.remove(base)

    #Allow the user to remove unwanted items (given as a list/iterable)
    if no_thanks == None:
        pass
    else:
        for food in no_thanks:
         food_choices.remove(food)


    #Where the magic happens
    while cal_count < calories:
        for choice in food_choices: 
            if cal_count + flavor[choice][0] <=  calories:  
                cal_count += flavor[choice][0]
                protein_count += flavor[choice][1]
                food_choices.remove(choice)
                meal.append(choice)
                break

            elif cal_count + flavor[choice][0] > calories and not(precise):
                return (meal, cal_count, protein_count)          

            else:   
                remaining = calories - cal_count
                protein_count += round(serving_scaler(choice, flavor, remaining)[1])
                gram_change = serving_scaler(choice, flavor, remaining)[2]
                cal_count = calories
                meal.append(choice)
                return (meal ,cal_count, protein_count, f'Use {round(gram_change)} grams of {meal[len(meal)-1]} to make it work')






pass
