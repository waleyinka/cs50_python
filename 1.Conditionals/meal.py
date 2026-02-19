# Task: https://cs50.harvard.edu/python/psets/1/meal/

def main():

    user_input = input("What time is it? ").strip()

    meal_time = convert(user_input)

    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")
    if 18.0 <= meal_time <= 19.0:
        print("dinner time")

def convert(time):

    hours, minutes = time.split(":")

    hours = float(hours)
    minutes = float(minutes) / 60

    return hours + minutes

if __name__ == "__main__":
    main()
