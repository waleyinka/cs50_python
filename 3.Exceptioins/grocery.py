# Task: https://cs50.harvard.edu/python/psets/3/grocery/


grocery_list = {}

while True:
    try:
        item = input().upper()

        if item in grocery_list:
            grocery_list[item] = grocery_list.get(item) + 1
        else:
            grocery_list[item] = 1

    except EOFError:
        for i in sorted(grocery_list):
            print(grocery_list[i], i)

        break