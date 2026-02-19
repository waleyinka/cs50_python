# Task: https://cs50.harvard.edu/python/psets/1/extensions/


def main():

    file_name = input("What is the name of your file? ").strip().lower()

    if file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith(".jpeg") or file_name.endswith(".jpg"):
        print("image/jpeg")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()