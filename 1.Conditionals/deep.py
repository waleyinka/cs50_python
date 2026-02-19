# Task: https://cs50.harvard.edu/python/psets/1/deep/


user_answer = input("The Answer to the Great Question of Life is? ").strip().lower()

match user_answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")