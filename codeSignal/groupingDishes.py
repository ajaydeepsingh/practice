"""
You are given a list dishes, where each element consists of a list of strings 
beginning with the name of the dish, followed by all the ingredients used in 
preparing it. You want to group the dishes by ingredients, so that for each 
ingredient you'll be able to find all the dishes that contain it (if there are 
at least 2 such dishes).

Return an array where each element is a list beginning with the ingredient name,
followed by the names of all the dishes that contain this ingredient. 
The dishes inside each list should be sorted lexicographically, and the 
result array should be sorted lexicographically by the names of the 
ingredients.



"""


def groupingDishes(dishes):

    fooddict = {}

    for dish in dishes:
        main_dish = dish[0]
        dish = dish[1:]

        for i, v in enumerate(dish):
            if v in fooddict:
                fooddict[v] = fooddict[v] + [main_dish]
            else:
                fooddict[v] = [main_dish]

    filter_dict = {}
    for k, v in fooddict.items():
        if len(v) > 1:
            filter_dict[k] = v


    new = sorted(filter_dict.items())
    arr =[]

    for i in new:
        arr.append([i[0],**sorted(i[1])])

    return arr